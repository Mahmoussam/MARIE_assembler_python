# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from QCodeEditor import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 931)
        MainWindow.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.codeEditor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.codeEditor=QCodeEditor(DISPLAY_LINE_NUMBERS=True, 
                             HIGHLIGHT_CURRENT_LINE=True,
                             SyntaxHighlighter=XMLHighlighter,Parent=self.centralwidget)
        self.codeEditor.setGeometry(QtCore.QRect(10, 10, 1091, 521))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.codeEditor.setFont(font)
        self.codeEditor.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);")
        self.codeEditor.setPlainText("")
        self.codeEditor.setObjectName("codeEditor")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 540, 971, 361))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_hex = QtWidgets.QWidget()
        self.tab_hex.setObjectName("tab_hex")
        self.hex_PText = QtWidgets.QPlainTextEdit(self.tab_hex)
        self.hex_PText.setGeometry(QtCore.QRect(0, 0, 971, 331))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.hex_PText.setFont(font)
        self.hex_PText.setStyleSheet("color:rgb(255, 255, 255)")
        self.hex_PText.setObjectName("hex_PText")
        self.tabWidget.addTab(self.tab_hex, "")
        self.tab_mc = QtWidgets.QWidget()
        self.tab_mc.setObjectName("tab_mc")
        self.mc_PText = QtWidgets.QPlainTextEdit(self.tab_mc)
        self.mc_PText.setGeometry(QtCore.QRect(0, 0, 971, 341))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.mc_PText.setFont(font)
        self.mc_PText.setStyleSheet("color:rgb(255, 255, 255)")
        self.mc_PText.setObjectName("mc_PText")
        self.tabWidget.addTab(self.tab_mc, "")
        self.assembleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.assembleBtn.setGeometry(QtCore.QRect(1000, 560, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.assembleBtn.setFont(font)
        self.assembleBtn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.045, x2:1, y2:0.0397727, stop:0 rgb(0, 200, 0), stop:1 rgb(0, 255, 0,));\n"
"color: rgb(255, 255, 255);")
        self.assembleBtn.setObjectName("assembleBtn")
        self.simulateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.simulateBtn.setGeometry(QtCore.QRect(1000, 610, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.simulateBtn.setFont(font)
        self.simulateBtn.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.simulateBtn.setObjectName("simulateBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mc_PText.setReadOnly(True)
        self.hex_PText.setReadOnly(True)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.codeEditor.setPlaceholderText(_translate("MainWindow", "Assembly code goes here"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hex), _translate("MainWindow", "Hex Code"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mc), _translate("MainWindow", "Machine Code"))
        self.assembleBtn.setText(_translate("MainWindow", "Assemble"))
        self.simulateBtn.setText(_translate("MainWindow", "Simulate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())