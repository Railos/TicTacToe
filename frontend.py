import ctypes
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

backend = ctypes.CDLL("C:/Users/Ivan/Desktop/TicTacToe/backend.so", winmode=0)
#когда изменен backend.cpp обязательно прописывать команду в терминале!!!
#g++ -fPIC -shared -o backend.so backend.cpp


class MainWindow(QMainWindow):
    singleton: 'MainWindow' = None

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TicTacToe")

        self.setFixedSize(QSize(640, 480))

        self.initUI()

    def initUI(self):
        self.button1 = QPushButton(self)
        self.button1.setGeometry(40, 40, 100, 50)
        self.button1.setText("1")
        self.button1.setStyleSheet('QPushButton {color: black; background-color: black; font-size: 45px;}')
        self.button1.setCheckable(True)

        self.button2 = QPushButton(self)
        self.button2.setGeometry(150, 40, 100, 50)
        self.button2.setText("2")
        self.button2.setStyleSheet('QPushButton {color: black; background-color: black; font-size: 45px;}')
        self.button2.setCheckable(True)

        self.button3 = QPushButton(self)
        self.button3.setGeometry(260, 40, 100, 50)
        self.button3.setText("3")
        self.button3.setStyleSheet('QPushButton {color: black; background-color: black; font-size: 45px;}')
        self.button3.setCheckable(True)

        self.button4 = QPushButton(self)
        self.button4.setGeometry(40, 100, 100, 50)
        self.button4.setText("4")
        self.button4.setStyleSheet('QPushButton {color: black; background-color: black; font-size: 45px;}')
        self.button4.setCheckable(True)

        self.button5 = QPushButton(self)
        self.button5.setGeometry(150, 100, 100, 50)
        self.button5.setText("5")
        self.button5.setStyleSheet('QPushButton {color: black; background-color: black; font-size: 45px;}')
        self.button5.setCheckable(True)

        self.button6 = QPushButton(self)
        self.button6.setGeometry(260, 100, 100, 50)
        self.button6.setText("6")
        self.button6.setStyleSheet('QPushButton {color: black; background-color: black; font-size: 45px;}')
        self.button6.setCheckable(True)

        self.button7 = QPushButton(self)
        self.button7.setGeometry(40, 160, 100, 50)
        self.button7.setText("7")
        self.button7.setStyleSheet('QPushButton {color: black; background-color: black; font-size: 45px;}')
        self.button7.setCheckable(True)

        self.button8 = QPushButton(self)
        self.button8.setGeometry(150, 160, 100, 50)
        self.button8.setText("8")
        self.button8.setStyleSheet('QPushButton {color: black; background-color: black; font-size: 45px;}')
        self.button8.setCheckable(True)

        self.button9 = QPushButton(self)
        self.button9.setGeometry(260, 160, 100, 50)
        self.button9.setText("9")
        self.button9.setStyleSheet('QPushButton {color: black; background-color: black; font-size: 45px;}')
        self.button9.setCheckable(True)

        self.gameState = QLabel(self)
        self.gameState.setGeometry(95,250,450,70)
        self.gameState.setStyleSheet('QLabel {color: black; font-size: 45px;}')

        self.resButton = QPushButton(self)
        self.resButton.setGeometry(95, 320, 100, 50)
        self.resButton.setText("Рестарт")
        self.resButton.setStyleSheet('QPushButton {color: black; font-size: 20px;}')
        self.resButton.setCheckable(True)
        self.resButton.clicked.connect(self.restart)

        self.group = QButtonGroup()
        self.group.addButton(self.button1)
        self.group.addButton(self.button2)
        self.group.addButton(self.button3)
        self.group.addButton(self.button4)
        self.group.addButton(self.button5)
        self.group.addButton(self.button6)
        self.group.addButton(self.button7)
        self.group.addButton(self.button8)
        self.group.addButton(self.button9)

        self.group.buttonClicked.connect(self.on_click)

        self.changeButtons(self,True)

        self.show()

    def on_click(self,btn):
        if backend.paintRect(int(btn.text())) == 0:
            btn.setStyleSheet('QPushButton {color: red; background-color: red; font-size: 45px;}')
            btn.setText("X");
            btn.setEnabled(False)
        else:
            btn.setStyleSheet('QPushButton {color: blue; background-color: blue; font-size: 45px;}')
            btn.setText("O");
            btn.setEnabled(False)

        isWon = backend.isGameOver()

        if isWon == 1:
            if backend.getHod() == 0:
                self.gameState.setText("Выиграли нолики!")
                self.changeButtons(self,False)
            else:
                self.gameState.setText("Выиграли крестики!")
                self.changeButtons(self,False)
        elif isWon == 2:
            self.gameState.setText("Ничья!")
            self.changeButtons(self,False)

    @staticmethod
    def changeButtons(self, b):
        self.button1.setEnabled(b)
        self.button2.setEnabled(b)
        self.button3.setEnabled(b)
        self.button4.setEnabled(b)
        self.button5.setEnabled(b)
        self.button6.setEnabled(b)
        self.button7.setEnabled(b)
        self.button8.setEnabled(b)
        self.button9.setEnabled(b)


    @staticmethod
    def restart():
        backend.restartGame()
        MainWindow.singleton = MainWindow()


app = QApplication([])
MainWindow.restart()
sys.exit(app.exec_())