import sys

# prefer official qt bindings
if 'PySide2' in sys.modules:
    from PySide2.QtWidgets import QApplication, QMainWindow
else:
    from PyQt5.QtWidgets import QApplication, QMainWindow
import client
import log
from ftp import FTP

logger = log.setup('ftp')


def test():
    logger.info("testing with 104.238.181.33:21")
    ftp = FTP("104.238.181.33")
    ftp.send("NOOP")
    ftp.recv(200)
    ftp.download('foo')
    # ftp.upload('bar')
    ftp.list()
    ftp.send("QUIT")
    ftp.recv(221)


def main(argv):
    app = QApplication(argv)
    main_window = QMainWindow()
    ui = client.Ui_MainWindow()
    ui.setupUi(main_window)
    qss_style = open('./ui/style.qss').read()
    main_window.setStyleSheet(qss_style)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test()
    # main(sys.argv)
