import sys
from cx_Freeze import setup, Executable

# from PySide2.QtWidgets import QApplication, QWidget, QAction, QSystemTrayIcon, QMenu
# from PySide2.QtGui import QIcon
# import socket


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {'packages': [], 'excludes': []}

setup(  name = '<displayIP>',
        version = '1.0.0.0',
        description = '<None>',
        options = {'build_exe': build_exe_options},
        executables = [Executable('displayIP.py')])