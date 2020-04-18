import socket

import log
import os

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
        ret = self.socket.recv(RECV_BUF_SZ).decode("utf-8").strip()
        logger.info(ret)
        if code is not None:
            # logger.info("expecting {} got {}".format(code, ret[:3]))
            assert ret[:3] == "{}".format(code), "expecting statue code {} got {}".format(code, ret[:3])
        return ret

    # extract host and port from the response
    # resp format: 227 xxx (host,port)
    def parse227(self, resp):
        assert resp[:3] == '227', "PASV mode change fail"

        import re
        _227_re = re.compile(r'(\d+),(\d+),(\d+),(\d+),(\d+),(\d+)', re.ASCII)
        
        m = _227_re.search(resp)
        assert m, "No match host and port"
        numbers = m.groups()
        host = '.'.join(numbers[:4])
        port = (int(numbers[4]) << 8) + int(numbers[5])
        return host, port

    # send PASV
    def makepasv(self):
        self.send('PASV')  # receive 227
        host,port = self.parse227(self.recv(227))
        return host,port

    # establish a new data connection
    # STOR and RETR
    # cmd： 'STOR name' or 'RETR name'
    def transfercmd(self, cmd):
        host, port = self.makepasv()
        conn = socket.create_connection((host, port))   # data connection
        self.send(cmd)
        self.recv(150)
        return conn

    # upload files by binary -- STOR
    def upload(self, b_url, e_url="", blocksize=8192):
        filename = os.path.basename(b_url)
        cmd = "STOR {}".format(e_url + '/' + filename)
        fp = open(b_url, 'rb')
        with self.transfercmd(cmd) as conn:
            while 1:
                pass
                buf = fp.read(blocksize)
                if not buf:
                    break
                conn.sendall(buf)
        fp.close()
        return self.recv() #226 Transfer complete


    # download files by binary -- RETR
    def download(self, b_url, e_url="", blocksize=8192):
        filename = os.path.basename(b_url)
        cmd = "RETR {}".format(b_url)
        fp = open(e_url + filename,'wb')
        with self.transfercmd(cmd) as conn:
            while 1:
                data = conn.recv(blocksize)
                if not data:
                    break
                fp.write(data)
        fp.close()
        return self.recv() #226 Transfer complete