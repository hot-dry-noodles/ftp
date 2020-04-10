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

    # send a ftp command to the server, CRLF would be automatically appended
    # `send` and `recv` are the two most fundamental abstraction over ftp communication model
    # most control message exchange can be expressed using these two methods
    def send(self, cmd: str):
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
