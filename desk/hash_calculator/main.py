from sys import argv

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (

QApplication, QMainWindow, QWidget,

QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,

QLabel, QLineEdit, QPushButton, QComboBox, QDockWidget, QListWidget,

QProgressBar, QFileDialog
)

from utils import FileCMPManager
from widgets import FileSelectButton


class CheckSumCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("FileCMP Manager | Hash calculator")
        self.setFixedSize(400, 600)
        self.setStyleSheet("background-color: #dddddd;")
        self.setWindowIcon(QIcon("res/icon.ico"))

        self.bufferSize: int = 0

        self.widget = QWidget()

        self.layout = QVBoxLayout()

        self.fileSelectButton = FileSelectButton()

        self.fileNameLabel = QLabel()
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

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

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
    gui = CheckSumCalculator()
    gui.show()
    app.exec()

if __name__ == '__main__': main()
