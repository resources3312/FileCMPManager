from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt, QSize



class FileSelectButton(QPushButton):
    
    def __init__(self, size=QSize(200, 200), crossColor="#222222", backgroundColor="#cccccc"):
        super().__init__()

        self.__size: QSize = size
        self.__backgroundColor: str = backgroundColor
        self.__crossColor: str = crossColor

        self.__filePath: str = ""
        self.setWaitStyle()
    
    def __clearWidget(self) -> None:
        self.setText("")
        self.setStyleSheet("background-color: none; border: none;")
        self.setIconSize(QSize(0, 0))
        self.setIcon(QIcon())

    def setWaitStyle(self) -> None:
        self.__clearWidget()
        self.setText("+")
        self.setFixedSize(self.__size)
        self.setStyleSheet(f"color: {self.__crossColor}; background-color: {self.__backgroundColor}; text-align: center; font-size: 150px; padding-bottom: 25px; border: none;")

    def setSelectedStyle(self) -> None:
        self.__clearWidget()
        self.setFixedSize(self.__size)
        self.setIconSize(self.__size)
        self.setIcon(QIcon("./res/fileSelected.ico"))
  

    def switchStyle(self) -> None:
        self.setSelectedStyle() if self.text() else self.setWaitStyle()



class ApplicationGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Отладка виджета FileSelectButton")
        
        self.widget = QWidget()
        self.layout = QVBoxLayout()

        self.btn = FileSelectButton()
        
        self.btn.clicked.connect(self.btn.switchStyle)

        self.layout.addWidget(self.btn)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

if __name__ == '__main__':
    app = QApplication([])
    gui = ApplicationGUI()
    gui.show()
    app.exec()
