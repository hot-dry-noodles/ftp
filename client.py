import sys

# prefer official qt bindings
if 'PySide2' in sys.modules:
    from PySide2 import QtWidgets, QtCore, QtGui
    from PySide2.QtWidgets import QInputDialog
else:
    from PyQt5 import QtWidgets, QtCore, QtGui
    from PyQt5.QtWidgets import QInputDialog
from utils import *
from ftp import *


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class Ui_MainWindow(object):
    ftp = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.runLabel = QtWidgets.QLabel(self.centralwidget)
        self.runLabel.setObjectName("runLabel")
        self.horizontalLayout_6.addWidget(self.runLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.runInfoOutput = QtWidgets.QTextBrowser(self.centralwidget)
        self.runInfoOutput.setEnabled(True)
        self.runInfoOutput.setObjectName("runInfoOutput")
        self.verticalLayout_4.addWidget(self.runInfoOutput)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.portLabel = QtWidgets.QLabel(self.centralwidget)
        self.portLabel.setObjectName("portLabel")
        self.horizontalLayout_2.addWidget(self.portLabel)
        self.portInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portInput.sizePolicy().hasHeightForWidth())
        self.portInput.setSizePolicy(sizePolicy)
        self.portInput.setObjectName("portInput")
        self.horizontalLayout_2.addWidget(self.portInput)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_7.addWidget(self.connectButton)
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy)
        self.disconnectButton.setObjectName("disconnectButton")
        self.horizontalLayout_7.addWidget(self.disconnectButton)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serverLabel = QtWidgets.QLabel(self.centralwidget)
        self.serverLabel.setObjectName("serverLabel")
        self.horizontalLayout.addWidget(self.serverLabel)
        self.serverInput = QtWidgets.QLineEdit(self.centralwidget)
        self.serverInput.setText("")
        self.serverInput.setObjectName("serverInput")
        self.horizontalLayout.addWidget(self.serverInput)
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setObjectName("userLabel")
        self.horizontalLayout.addWidget(self.userLabel)
        self.userInput = QtWidgets.QLineEdit(self.centralwidget)
        self.userInput.setText("")
        self.userInput.setObjectName("userInput")
        self.horizontalLayout.addWidget(self.userInput)
        self.passwdLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwdLabel.setObjectName("passwdLabel")
        self.horizontalLayout.addWidget(self.passwdLabel)
        self.passwdInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwdInput.setText("")
        self.passwdInput.setObjectName("passwdInput")
        self.horizontalLayout.addWidget(self.passwdInput)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.localLabel = QtWidgets.QLabel(self.centralwidget)
        self.localLabel.setObjectName("localLabel")
        self.horizontalLayout_3.addWidget(self.localLabel)
        self.localPathInput = QtWidgets.QLineEdit(self.centralwidget)
        self.localPathInput.setText("")
        self.localPathInput.setObjectName("localPathInput")
        self.horizontalLayout_3.addWidget(self.localPathInput)
        self.localPathButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localPathButton.sizePolicy().hasHeightForWidth())
        self.localPathButton.setSizePolicy(sizePolicy)
        self.localPathButton.setObjectName("localPathButton")
        self.horizontalLayout_3.addWidget(self.localPathButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.localFileList = QtWidgets.QTableView(self.centralwidget)
        self.localFileList.setObjectName("localFileList")
        self.verticalLayout_2.addWidget(self.localFileList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.remoteLabel = QtWidgets.QLabel(self.centralwidget)
        self.remoteLabel.setObjectName("remoteLabel")
        self.horizontalLayout_5.addWidget(self.remoteLabel)
        self.remotePathInput = QtWidgets.QLineEdit(self.centralwidget)
        self.remotePathInput.setText("")
        self.remotePathInput.setObjectName("remotePathInput")
        self.horizontalLayout_5.addWidget(self.remotePathInput)
        self.remotePathButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remotePathButton.sizePolicy().hasHeightForWidth())
        self.remotePathButton.setSizePolicy(sizePolicy)
        self.remotePathButton.setObjectName("remotePathButton")
        self.horizontalLayout_5.addWidget(self.remotePathButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.remoteFileList = QtWidgets.QTableView(self.centralwidget)
        self.remoteFileList.setObjectName("remoteFileList")
        self.verticalLayout_3.addWidget(self.remoteFileList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # modified part start
        self.passwdInput.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.localPathInput.setText(LOCAL_DEFAULT_PATH)
        self.localModel = QtGui.QStandardItemModel()
        self.remoteModel = QtGui.QStandardItemModel()
        self.showLocalList()
        self.showRemoteList()
        self.localFileList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.localFileList.customContextMenuRequested.connect(self.createLocalContextMenu)
        self.remoteFileList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.remoteFileList.customContextMenuRequested.connect(self.createRemoteContextMenu)
        self.connectButton.clicked.connect(self.connectHandler)
        self.disconnectButton.clicked.connect(self.disconnectHandler)
        self.localPathButton.clicked.connect(self.changeLocalPath)
        self.remotePathButton.clicked.connect(self.changeRemotePath)
        self.localFileList.doubleClicked.connect(self.localDoubleClick)
        self.remoteFileList.doubleClicked.connect(self.remoteDoubleClick)
        # modified part end
        # self.ftp = FTP('192.168.0.106', user='kenvis', passwd='ks8449922123')
        '''
        redirecting stdout and stderr to runInfoOutput
        '''
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FTP客户端"))
        self.serverLabel.setText(_translate("MainWindow", "主机"))
        self.userLabel.setText(_translate("MainWindow", "用户名"))
        self.passwdLabel.setText(_translate("MainWindow", "密码"))
        self.portLabel.setText(_translate("MainWindow", "端口号"))
        self.runLabel.setText(_translate("MainWindow", "运行信息"))
        self.localLabel.setText(_translate("MainWindow", "本机路径"))
        self.localPathButton.setText(_translate("MainWindow", "确定"))
        self.remoteLabel.setText(_translate("MainWindow", "远程路径"))
        self.remotePathButton.setText(_translate("MainWindow", "确定"))
        self.connectButton.setText(_translate("MainWindow", "连接"))
        self.disconnectButton.setText(_translate("MainWindow", "断开"))

    '''
    above codes are generated automatically.
    only modify codes below.
    '''

    def connectHandler(self):
        host = self.serverInput.text()
        user = self.userInput.text()
        passwd = self.passwdInput.text()
        # port = self.portInput.text()
        if user == '':
            self.ftp = FTP(host)
        else:
            self.ftp = FTP(host, user=user, passwd=passwd)
        self.showRemoteList()
        self.remotePathInput.setText(self.ftp.pwd())

    def disconnectHandler(self):
        self.ftp.send("QUIT")
        self.ftp.recv(221)
        self.ftp = None
        self.showRemoteList()

    def localDoubleClick(self):
        index = self.localFileList.currentIndex()
        row = index.row()
        if row == 0:
            path = os.path.dirname(self.localPathInput.text())
            self.localPathInput.setText(path)
            self.showLocalList(path)
            return
        path = self.localPathInput.text() + '/'
        path += self.localModel.index(row, 0).data()
        mode = self.localModel.index(row, 3).data()
        if mode.startswith('d'):
            self.localPathInput.setText(path)
            self.showLocalList(path)

    def remoteDoubleClick(self):
        index = self.remoteFileList.currentIndex()
        row = index.row()
        if row == 0:
            self.ftp.cd('..')
            path = self.ftp.pwd()
            self.remotePathInput.setText(path)
            self.showRemoteList(path)
            return
        path = self.ftp.pwd() + '/'
        path += self.remoteModel.index(row, 0).data()
        mode = self.remoteModel.index(row, 3).data()
        if mode.startswith('d'):
            self.remotePathInput.setText(path)
            self.ftp.cd(path)
            self.showRemoteList(path)

    def changeLocalPath(self):
        local_path = self.localPathInput.text()
        self.showLocalList(local_path)

    def changeRemotePath(self):
        remote_path = self.remotePathInput.text()
        self.showRemoteList(remote_path)

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
        removeAction.triggered.connect(self.localRemoveHandler)
        mkdirAction.triggered.connect(self.localMkdirHandler)
        uploadAction.triggered.connect(self.uploadHandler)
        renameAction.triggered.connect(self.localRenameHandler)
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
        removeAction.triggered.connect(self.remoteRemoveHandler)
        mkdirAction.triggered.connect(self.remoteMkdirHandler)
        downloadAction.triggered.connect(self.downloadHandler)
        renameAction.triggered.connect(self.remoteRenameHandler)
        refreshAction.triggered.connect(self.remoteRefreshHandler)
        remoteMenu.exec_(QtGui.QCursor.pos())

    def showLocalList(self, path=''):
        self.localModel.clear()
        self.localModel.setHorizontalHeaderLabels((u'文件名', u'文件大小', u'文件类型', u'文件权限', u'修改日期'))
        self.localFileList.setModel(self.localModel)
        self.localFileList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.localFileList.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.localFileList.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.localFileList.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.localFileList.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.localItems = ListFolder(path)
        for i in range(0, len(self.localItems)):
            self.localModel.insertRow(i, self.localItems[i])

    def showRemoteList(self, path=''):
        self.remoteModel.clear()
        self.remoteModel.setHorizontalHeaderLabels((u'文件名', u'文件大小', u'文件类型', u'文件权限', u'修改日期'))
        self.remoteFileList.setModel(self.remoteModel)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.remoteFileList.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        if self.ftp is not None:
            files = self.ftp.list(path)
            self.remoteItems = remoteListFolder(files)
            for i in range(0, len(self.remoteItems)):
                self.remoteModel.insertRow(i, self.remoteItems[i])

    def normalOutputWritten(self, text):
        cursor = self.runInfoOutput.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.runInfoOutput.setTextCursor(cursor)
        self.runInfoOutput.ensureCursorVisible()

    def localRemoveHandler(self):
        pass

    def remoteRemoveHandler(self):
        index = self.remoteFileList.currentIndex()
        row = index.row()
        filename = self.remoteModel.index(row, 0).data()
        self.ftp.rm(filename)
        self.showRemoteList()

    def localMkdirHandler(self):
        pass

    def remoteMkdirHandler(self):
        text, pressed = QInputDialog.getText(self.centralwidget, "mkdir", "enter new dir name:")
        if pressed and text != "":
            self.ftp.mkdir(text)
        self.showRemoteList()

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

    def localRenameHandler(self):
        pass

    def remoteRenameHandler(self):
        index = self.remoteFileList.currentIndex()
        row = index.row()
        filename = self.remoteModel.index(row, 0).data()
        text, pressed = QInputDialog.getText(self.centralwidget, "mv", "enter new file name:")
        if pressed and text != "":
            self.ftp.mv(filename, text)
        self.showRemoteList()

    def localRefreshHandler(self):
        pass

    def remoteRefreshHandler(self):
        self.showRemoteList()
