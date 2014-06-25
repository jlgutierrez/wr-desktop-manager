from PyQt4 import QtCore, QtGui
from frontend import Ui_MainWindow

import netsnmp, sys



class GetOIDsWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.lineEditOID.setText("iso.3.6.1.2.1.25.1.4.0")
        self.lineEditIP.setText("localhost")
        #self.getOIDsButton.connect(self.lineEdit, getOIDs(self))
    
        self.ButtongetOIDs.clicked.connect(self.ButtongetOIDs_clicked)
                    
    
    # Getting all available OIDs
    def getOIDsButton_clicked(self):
        if(self.lineEditIP.text() <> ""):
            ip = str(self.lineEditOID.text())
            vars =  netsnmp.VarList( netsnmp.Varbind('ifDescr'))
            res  = netsnmp.snmpwalk( vars, Version = 1, DestHost = ip, Community = 'public' )
            print res
        else:
            print "IP Required!"
    
    # Getting OID info        
    def ButtongetOIDs_clicked(self):
        if ((self.lineEditIP.text() <> "") and (self.lineEditOID.text() <> "")):
            ip = str(self.lineEditIP.text())
            oid =  str(self.lineEditOID.text())
            session = netsnmp.Session( DestHost=ip, Version=2, Community='public' )
            vars = netsnmp.VarList( netsnmp.Varbind(oid) )
            #vars = netsnmp.snmpwalk(netsnmp.Varbind(oid), DestHost=ip, Version=2, Community='public')
            #for item in vars:
            self.textBrowserResult.setText(str(session.get(vars)))
        else:
            print "IP and OID Required!"
            

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    MainApp = GetOIDsWindow()
    MainApp.show()
    sys.exit(app.exec_())
    
    