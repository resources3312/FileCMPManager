from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (

QApplication, QMainWindow, QWidget,

QVBoxLayout, QHBoxLayout, QGridLayout,

QLabel, QLineEdit,

QFileDialog, QDialog
)



class ApplicationGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("FileCMP Manager v1.0")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #dddddd;")
        self.setWindowIcon(QIcon("res/icon.ico"))
        
        

def main() -> None:
    app = QApplication([])
    interface = ApplicationGUI()
    interface.show()
    app.exec()

if __name__ == '__main__': main()
