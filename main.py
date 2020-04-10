import log
import sys
import client
from PyQt5.QtWidgets import QApplication, QMainWindow
from ftp import FTP

logger = log.setup('ftp')


def test():
    logger.info("testing with 104.238.181.33:21")
    ftp = FTP("104.238.181.33")
    ftp.send("NOOP")
    ftp.recv(200)
    ftp.send("NOOP")
    ftp.recv(200)
    ftp.send("QUIT")
    ftp.recv(221)


def main():
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = client.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
