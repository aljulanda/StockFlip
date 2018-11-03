#!/usr/bin/python3
# -*- coding: utf-8 -*-

version = "0.1"
title = "StockFlip - version " + version

import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5
from PyQt5.QtWidgets import *

class Login_UI(QDialog):
    def __init__(self):
        super().__init__()
        ui = uic.loadUi('UI/login_dialog.ui', baseinstance=self)
        ui.LoginButton.clicked.connect(self.perform_login)

    def perform_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        #Login.blah blah blah
        print("Perform login here")
        self.accept()
 
class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = title
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.centerScreen()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit?',
            "Are you sure to quit?", QMessageBox.No | 
            QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def centerScreen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login_UI()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        mainApp = MainApp()
        mainApp.show()
        sys.exit(app.exec_())

