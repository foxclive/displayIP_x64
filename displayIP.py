from PySide2.QtWidgets import QApplication, QWidget, QAction, QSystemTrayIcon, QMenu 
from PySide2.QtGui import QIcon, QClipboard
from PySide2.QtCore import Slot, SIGNAL
from socket import socket, AF_INET, SOCK_DGRAM

import sys

class LauncherIP:
    def __init__(self):
        try:
            s=socket(AF_INET, SOCK_DGRAM)
            s.connect(('114.114.114.114',80))
            self.ip=s.getsockname()[0]
        finally:
            s.close()
    #获取系统IP
    def test(self):
        print("testing")

    def fouceEx(self):
        sys.exit()

    def copy(self):
        cb = QClipboard()
        try:
            cb.setText(self.ip)
            lable
        except:
            self.fouceEx()


    def Ui(self):
        app = QApplication(sys.argv)
        W=QWidget()

        #生成动作
        act_copy=QAction('复制到剪切板')
        act_about=QAction("关于: 0.1    FoxZno")
        act_exit=QAction("退出")
        act_copy.triggered.connect(self.copy)
        act_exit.triggered.connect(self.fouceEx)
    
        tray=QSystemTrayIcon(W)
        tray.setToolTip(self.ip)
        tray.setIcon(QIcon('.\icon\ip.png'))
        tray.setVisible(True)
        trayMenu=QMenu()


        #添加动作
        trayMenu.addAction(act_copy)
        trayMenu.addAction(act_about)
        trayMenu.addAction(act_exit)
        
        tray.setContextMenu(trayMenu)
        sys.exit(app.exec_())



def main():
    if __name__ == "__main__":
        ui=LauncherIP()
        ui.Ui()
        

main()
