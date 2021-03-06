import os
import re
import socket

import log

logger = log.get("ftp")

CRLF = "\r\n"
FTP_PORT = 21
RECV_BUF_SZ = 1024


class FTP:
    host = None
    port = FTP_PORT
    socket = None
    user = "anonymous"
    passwd = ""
    sock_file = ""

    def __init__(self, host, port=None, user=None, passwd=None):
        self.host = host
        if port is not None:
            self.port = port
        if user is not None:
            self.user = user
        if passwd is not None:
            self.passwd = passwd
        self.connect()
        self.login()

    def connect(self):
        self.socket = socket.create_connection((self.host, self.port))
        self.sock_file = self.socket.makefile('r')
        self.recv(220)

    def login(self):
        self.send("USER {}".format(self.user))
        self.recv(331)
        self.send("PASS {}".format(self.passwd))
        self.recv(230)

    def list(self):
        self.send("USER {}".format(self.user))
        self.recv(331)

    # send a ftp command to the server, CRLF would be automatically appended
    # `send` and `recv` are the two most fundamental abstraction over ftp communication model
    # most control message exchange can be expressed using these two methods
    def send(self, cmd: str):
        cmd = cmd.strip()
        logger.info(cmd)
        self.socket.send(bytes("{}".format(cmd) + CRLF, "utf-8"))

    # receive the server respond and check its legality when status code is offered
    def recv(self, code=None) -> str:
        ret = self.sock_file.readline().strip()
        logger.info(ret)
        if code is not None:
            # logger.info("expecting {} got {}".format(code, ret[:3]))
            assert ret[:3] == "{}".format(code), "expecting statue code {} got {}".format(code, ret[:3])
        return ret

    # extract host and port from the response
    # resp format: 227 (h3, h2, h1, h0, p1, p0)
    def parse227(self, resp) -> (str, int):
        _227_re = re.compile(r'(\d+),(\d+),(\d+),(\d+),(\d+),(\d+)', re.ASCII)
        m = _227_re.search(resp)
        assert m, "server did not respond with a valid socket address"
        numbers = list(map(int, m.groups()))
        host = '.'.join(map(str, numbers[:4]))
        port = (numbers[4] << 8) + numbers[5]
        return host, port

    # enter passive mode for data transfer
    def pasv(self) -> (str, int):
        self.send('PASV')  # receive 227
        host, port = self.parse227(self.recv(227))
        return host, port

    # establish a new data connection
    # cmd can be one of:
    # STOR name: Accept the data and to store the data as a file at the server site
    # RETR name: Retrieve a copy of the file
    def transfer(self, cmd) -> socket:
        self.send("TYPE I")  # binary mode
        self.recv(200)
        host, port = self.pasv()
        self.send(cmd)
        conn = socket.create_connection((host, port))  # data connection
        self.recv(150)  # File status okay; about to open data connection.
        return conn

    # upload files by binary -- STOR
    def upload(self, local, remote="", blocksize=8192):
        path = remote + os.path.basename(local)
        self.send("SIZE {}".format(path))
        try:
            offset = int(self.recv(213)[3:].strip())
        except AssertionError:
            offset = 0
        # logger.info("offset {}".format(offset))
        with open(local, 'rb') as f, self.transfer("APPE {}".format(path)) as conn:
            f.seek(offset)
            while 1:
                buf = f.read(blocksize)
                if not buf:
                    break
                logger.info("sent {} bytes".format(len(buf)))
                # logger.info("sent {}".format(buf))
                conn.sendall(buf)
        self.recv(226)  # Closing data connection

    # download files by binary -- RETR
    def download(self, remote, local="", blocksize=8192):
        filename = os.path.basename(remote)
        cmd = "RETR {}".format(remote)
        path = local + filename
        # reset offset to where previous transmission ends
        retry = os.path.exists(path)
        if retry:
            offset = os.stat(path).st_size
            self.send("REST {}".format(offset))
            self.recv(350)
        with open(path, 'ab' if retry else 'wb') as f, self.transfer(cmd) as conn:
            while 1:
                buf = conn.recv(blocksize)
                logger.info("received {} bytes".format(len(buf)))
                if not buf:
                    break
                logger.info("received {} bytes".format(len(buf)))
                f.write(buf)
        self.recv(226)  # 226 Transfer complete

    def list(self, path="") -> list:
        cmd = "LIST {}".format(path)
        lines = []
        with self.transfer(cmd) as conn:
            with conn.makefile('r') as f:
                lines = f.readlines()
        self.recv(226)
        files = list(map(lambda line: line.strip().split(), lines))
        filenames = list(map(lambda line: line[-1], files))
        logger.info("file list {}".format(filenames))
        return files

    def pwd(self):
        self.send("PWD")
        ret = self.recv(257)
        path = ret.split()[1]
        path = path[1:-1]
        return path

    def cd(self, path=""):
        self.send("CWD {}".format(path))
        self.recv(250)

    def mkdir(self, path):
        self.send("MKD {}".format(path))
        self.recv(257)

    def rm(self, path):
        try:
            self.send("DELE {}".format(path))
            self.recv(250)
        except AssertionError:
            self.send("RMD {}".format(path))
            self.recv(250)

    def mv(self, old, new):
        self.send("RNFR {}".format(old))
        self.recv(350)
        self.send("RNTO {}".format(new))
        self.recv(250)
