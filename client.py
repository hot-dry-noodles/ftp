import sys

# prefer official qt bindings
if 'PySide2' in sys.modules:
    from PySide2 import QtWidgets, QtCore, QtGui
else:
    from PyQt5 import QtWidgets, QtCore, QtGui
from utils import *
from ftp import *


class Ui_MainWindow(object):
    ftp = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serverLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.serverLabel.setObjectName("serverLabel")
        self.horizontalLayout.addWidget(self.serverLabel)
        self.serverInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.serverInput.setText("")
        self.serverInput.setObjectName("serverInput")
        self.horizontalLayout.addWidget(self.serverInput)
        self.userLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.userLabel.setObjectName("userLabel")
        self.horizontalLayout.addWidget(self.userLabel)
        self.userInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.userInput.setText("")
        self.userInput.setObjectName("userInput")
        self.horizontalLayout.addWidget(self.userInput)
        self.passwdLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.passwdLabel.setObjectName("passwdLabel")
        self.horizontalLayout.addWidget(self.passwdLabel)
        self.passwdInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.passwdInput.setText("")
        self.passwdInput.setObjectName("passwdInput")
        self.horizontalLayout.addWidget(self.passwdInput)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(550, 10, 111, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.portLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.portLabel.setObjectName("portLabel")
        self.horizontalLayout_2.addWidget(self.portLabel)
        self.portInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.portInput.setObjectName("portInput")
        self.horizontalLayout_2.addWidget(self.portInput)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 440, 1131, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.runLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.runLabel.setObjectName("runLabel")
        self.horizontalLayout_6.addWidget(self.runLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.runInfoOutput = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.runInfoOutput.setEnabled(True)
        self.runInfoOutput.setObjectName("runInfoOutput")
        self.verticalLayout_4.addWidget(self.runInfoOutput)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(670, 15, 71, 31))
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 50, 1131, 381))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.localLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.localLabel.setObjectName("localLabel")
        self.horizontalLayout_3.addWidget(self.localLabel)
        self.localPathInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.localPathInput.setText("")
        self.localPathInput.setObjectName("localPathInput")
        self.horizontalLayout_3.addWidget(self.localPathInput)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.localFileList = QtWidgets.QTableView(self.horizontalLayoutWidget_3)
        self.localFileList.setObjectName("localFileList")
        self.verticalLayout_2.addWidget(self.localFileList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.remoteLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.remoteLabel.setObjectName("remoteLabel")
        self.horizontalLayout_5.addWidget(self.remoteLabel)
        self.remotePathInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.remotePathInput.setText("")
        self.remotePathInput.setObjectName("remotePathInput")
        self.horizontalLayout_5.addWidget(self.remotePathInput)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.remoteFileList = QtWidgets.QTableView(self.horizontalLayoutWidget_3)
        self.remoteFileList.setObjectName("remoteFileList")
        self.verticalLayout_3.addWidget(self.remoteFileList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # modified part start
        self.localPathInput.setText(LOCAL_DEFAULT_PATH)
        self.localModel = QtGui.QStandardItemModel()
        self.remoteModel = QtGui.QStandardItemModel()
        self.showLocalList()
        self.showRemoteList()
        self.localFileList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.localFileList.customContextMenuRequested.connect(self.createLocalContextMenu)
        self.remoteFileList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.remoteFileList.customContextMenuRequested.connect(self.createRemoteContextMenu)
        # modified part end
        #self.ftp = FTP('192.168.0.106', user='kenvis', passwd='ks8449922123')
        self.showRemoteList()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FTP客户端"))
        self.serverLabel.setText(_translate("MainWindow", "主机"))
        self.userLabel.setText(_translate("MainWindow", "用户名"))
        self.passwdLabel.setText(_translate("MainWindow", "密码"))
        self.portLabel.setText(_translate("MainWindow", "端口号"))
        self.connectButton.setText(_translate("MainWindow", "连接"))
        self.localLabel.setText(_translate("MainWindow", "本机路径"))
        self.remoteLabel.setText(_translate("MainWindow", "远程路径"))
        self.runLabel.setText(_translate("MainWindow", "运行信息"))
        self.connectButton.clicked.connect(self.connectserver)

    '''
    above codes are generated automatically.
    only modify codes below.
    '''
    def connectserver(self):
        host = self.serverInput.text()
        user = self.userInput.text()
        passwd = self.passwdInput.text()
        #port = self.portInput.text()
        if user == '':
            self.ftp = FTP(host)
        else:
            self.ftp = FTP(host, user=user, passwd=passwd)
        self.showRemoteList()

    def createLocalContextMenu(self):
        localMenu = QtWidgets.QMenu(self.localFileList)
        removeAction = QtWidgets.QAction(u'删除')
        mkdirAction = QtWidgets.QAction(u'新建文件夹')
        uploadAction = QtWidgets.QAction(u'上传')
        renameAction = QtWidgets.QAction(u'重命名')
        refreshAction = QtWidgets.QAction(u'刷新')
        localMenu.addAction(removeAction)
        localMenu.addAction(mkdirAction)
        localMenu.addAction(uploadAction)
        localMenu.addAction(renameAction)
        localMenu.addAction(refreshAction)
        removeAction.triggered.connect(self.removeHandler)
        mkdirAction.triggered.connect(self.mkdirHandler)
        uploadAction.triggered.connect(self.uploadHandler)
        renameAction.triggered.connect(self.renameHandler)
        refreshAction.triggered.connect(self.localRefreshHandler)
        localMenu.exec_(QtGui.QCursor.pos())

    def createRemoteContextMenu(self):
        remoteMenu = QtWidgets.QMenu(self.remoteFileList)
        removeAction = QtWidgets.QAction(u'删除')
        mkdirAction = QtWidgets.QAction(u'新建文件夹')
        downloadAction = QtWidgets.QAction(u'下载')
        renameAction = QtWidgets.QAction(u'重命名')
        refreshAction = QtWidgets.QAction(u'刷新')
        remoteMenu.addAction(removeAction)
        remoteMenu.addAction(mkdirAction)
        remoteMenu.addAction(downloadAction)
        remoteMenu.addAction(renameAction)
        remoteMenu.addAction(refreshAction)
        removeAction.triggered.connect(self.removeHandler)
        mkdirAction.triggered.connect(self.mkdirHandler)
        downloadAction.triggered.connect(self.downloadHandler)
        renameAction.triggered.connect(self.renameHandler)
        refreshAction.triggered.connect(self.remoteRefreshHandler)
        remoteMenu.exec_(QtGui.QCursor.pos())

    def showLocalList(self):
        self.localModel.clear()
        self.localModel.setHorizontalHeaderLabels((u'文件名', u'文件大小', u'文件类型', u'文件权限', u'修改日期'))
        self.localFileList.setModel(self.localModel)
        self.localFileList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.localFileList.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.localFileList.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.localFileList.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.localFileList.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.localItems = ListFolder()
        for i in range(0, len(self.localItems)):
            self.localModel.insertRow(i, self.localItems[i])

    def showRemoteList(self):
        self.remoteModel.clear()
        self.remoteModel.setHorizontalHeaderLabels((u'文件名', u'文件大小', u'文件类型', u'文件权限', u'修改日期'))
        self.remoteFileList.setModel(self.remoteModel)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        if self.ftp is not None:
            files = self.ftp.list()
            self.remoteItems = remoteListFolder(files)
            for i in range(0, len(self.remoteItems)):
                self.remoteModel.insertRow(i, self.remoteItems[i])

    def removeHandler(self):
        pass

    def mkdirHandler(self):
        pass

    def uploadHandler(self):
        index = self.localFileList.currentIndex()
        row = index.row()
        filename = self.localModel.index(row, 0).data()  # file name
        localpath = self.localPathInput.text()
        filepath = localpath + '\\' + filename
        self.ftp.upload(filepath)
        self.showRemoteList()

    def downloadHandler(self):
        index = self.remoteFileList.currentIndex()
        row = index.row()
        filename = self.remoteModel.index(row, 0).data()
        self.ftp.download(filename)
        self.showLocalList()

    def renameHandler(self):
        pass

    def localRefreshHandler(self):
        pass

    def remoteRefreshHandler(self):
        pass
