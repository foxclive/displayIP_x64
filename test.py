from PySide2.QtWidgets import QApplication, QWidget, QAction, QSystemTrayIcon, QMenu 
from PySide2.QtGui import QIcon, QClipboard
from PySide2.QtCore import Slot, SIGNAL
from socket import socket, AF_INET, SOCK_DGRAM
import threading
import time
import sys

class IPtray:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Lock=threading.RLock()
        self.ip="0.0.0.0"
        self.app = QApplication(sys.argv)
        self.wMain=QWidget()
        self.tray=QSystemTrayIcon(self.wMain)
        

    def Ui(self):
        self.sub_getIP()
        self.sub_setToolTip()
        self.actExit=QAction("退出")
        self.tray.setIcon(QIcon('.\icon\ip.png'))
        self.tray.setVisible(True)
        self.trayMenu=QMenu()
        self.trayMenu.addAction(self.actExit)
        self.tray.setContextMenu(self.trayMenu)
        self.tray.showMessage("IP","你的IP是"+self.ip)
        sys.exit(self.app.exec_())

    def getIP(self):
        # self.Lock.acquire()
        while(1):
            try:
                s=socket(AF_INET, SOCK_DGRAM)
                s.connect(('114.114.114.114',80))
                self.ip=s.getsockname()[0]
            finally:
                s.close()
                print("exit getIP")
            time.sleep(5)
            # self.Lock.release()

    def setToolTip(self):
        while(1):
            self.tray.setToolTip(self.ip)
            print("exit setToopTip")
            time.sleep(5)

    def sub_getIP(self):
        self.subThread_getIP=threading.Thread(target=self.getIP)
        self.subThread_getIP.setDaemon=(True)
        self.subThread_getIP.start()
#这个线程要一直运行
    def sub_setToolTip(self):
        self.subThread_setToolTip=threading.Thread(target=self.setToolTip)
        self.subThread_setToolTip.setDaemon(True)
        self.subThread_setToolTip.start()

def main():
    if __name__ == "__main__":
        ui=IPtray()
        ui.Ui()

main()
