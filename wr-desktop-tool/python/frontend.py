# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_guis/frontend.ui'
#
# Created: Wed Jun 25 18:27:19 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.listViewMIBs = QtGui.QListView(self.tab)
        self.listViewMIBs.setGeometry(QtCore.QRect(10, 80, 301, 411))
        self.listViewMIBs.setObjectName(_fromUtf8("listViewMIBs"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(120, 60, 81, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setGeometry(QtCore.QRect(20, 10, 481, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditIP = QtGui.QLineEdit(self.splitter)
        self.lineEditIP.setObjectName(_fromUtf8("lineEditIP"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEditOID = QtGui.QLineEdit(self.splitter)
        self.lineEditOID.setObjectName(_fromUtf8("lineEditOID"))
        self.comboBoxSNMPOptions = QtGui.QComboBox(self.tab)
        self.comboBoxSNMPOptions.setGeometry(QtCore.QRect(533, 10, 121, 27))
        self.comboBoxSNMPOptions.setObjectName(_fromUtf8("comboBoxSNMPOptions"))
        self.comboBoxSNMPOptions.addItem(_fromUtf8(""))
        self.comboBoxSNMPOptions.addItem(_fromUtf8(""))
        self.comboBoxSNMPOptions.addItem(_fromUtf8(""))
        self.comboBoxSNMPOptions.addItem(_fromUtf8(""))
        self.ButtongetOIDs = QtGui.QPushButton(self.tab)
        self.ButtongetOIDs.setGeometry(QtCore.QRect(660, 10, 85, 27))
        self.ButtongetOIDs.setObjectName(_fromUtf8("ButtongetOIDs"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 40, 781, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.textBrowserResult = QtGui.QTextBrowser(self.tab)
        self.textBrowserResult.setGeometry(QtCore.QRect(330, 80, 441, 411))
        self.textBrowserResult.setObjectName(_fromUtf8("textBrowserResult"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(340, 60, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuConnect = QtGui.QMenu(self.menubar)
        self.menuConnect.setObjectName(_fromUtf8("menuConnect"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionIP_Address = QtGui.QAction(MainWindow)
        self.actionIP_Address.setObjectName(_fromUtf8("actionIP_Address"))
        self.actionSPEC_Card = QtGui.QAction(MainWindow)
        self.actionSPEC_Card.setObjectName(_fromUtf8("actionSPEC_Card"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuConnect.addAction(self.actionIP_Address)
        self.menuConnect.addAction(self.actionSPEC_Card)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConnect.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "SNMP MIBs", None))
        self.label.setText(_translate("MainWindow", "IP Address", None))
        self.label_2.setText(_translate("MainWindow", "OID:", None))
        self.comboBoxSNMPOptions.setItemText(0, _translate("MainWindow", "Get", None))
        self.comboBoxSNMPOptions.setItemText(1, _translate("MainWindow", "Get Next", None))
        self.comboBoxSNMPOptions.setItemText(2, _translate("MainWindow", "Get Bulk", None))
        self.comboBoxSNMPOptions.setItemText(3, _translate("MainWindow", "Walk", None))
        self.ButtongetOIDs.setText(_translate("MainWindow", "Go", None))
        self.label_4.setText(_translate("MainWindow", "Result", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Network Management", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Network Architecture", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Network Tools", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Help", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuConnect.setTitle(_translate("MainWindow", "Connect", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionImport.setText(_translate("MainWindow", "Import", None))
        self.actionExport.setText(_translate("MainWindow", "Export", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionIP_Address.setText(_translate("MainWindow", "White-Rabbit Switch", None))
        self.actionSPEC_Card.setText(_translate("MainWindow", "SPEC Card", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

