from sys import argv

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (

QApplication, QMainWindow, QWidget,

QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,

QLabel, QLineEdit, QPushButton, QComboBox, QDockWidget, QListWidget,

QProgressBar, QFileDialog, QDialog
)

from utils import FileCMPManager
from widgets import *



class CheckSumCalculator(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("FileCMP Manager | Hash calculator")
        self.setFixedSize(400, 600)
        self.setStyleSheet("background-color: #dddddd;")
        self.setWindowIcon(QIcon("res/icon.ico"))

        self.bufferSize: int = 0

        self.layout = QVBoxLayout()

        self.fileSelectButton = FileSelectButton()

        self.fileNameLabel = TitleLabel()
        self.fileNameLabel.setFixedSize(375, 50)
        self.fileNameLabel.setStyleSheet("font-weight: bold; font-size: 30px;")
        self.fileNameLabel.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.fileNameLabel.setText("Choose file to get hash")

        self.outputEntry = QLineEdit()
        self.outputEntry.setPlaceholderText("Hash is here")
        self.outputEntry.setReadOnly(True)

        self.fileSelectButton.clicked.connect(self.calculateCheckSum)

        self.layout.addWidget(self.fileSelectButton, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.fileNameLabel, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.outputEntry)

        self.setLayout(self.layout)


    def calculateCheckSum(self):
        try:
            self.fileSelectButton.setWaitStyle()

            self.fileNameLabel.setText("Choose file to get hash")
            self.outputEntry.clear()

            path = QFileDialog.getOpenFileName(self, "Выберите файл", "")

            self.fileNameLabel.setText(path[0].split("/")[len(path[0].split("/")) - 1])
            self.outputEntry.setText(FileCMPManager.getFileCheckSum(path=path[0], formatHex=True))

            self.fileSelectButton.setSelectedStyle()
        
        except:
            self.fileSelectButton.setWaitStyle()
            self.fileNameLabel.setText("Choose file to get hash")



def main() -> None:
    app = QApplication(argv)
    interface = CheckSumCalculator()
    interface.show()
    app.exec()

if __name__ == '__main__': main()
