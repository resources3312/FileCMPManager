from PyQt6.QtWidgets import (
QApplication, QMainWindow, QWidget,
QVBoxLayout,
QLabel, QPushButton)

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt, QSize



class MenuIcon(QPushButton):
    def __init__(self, utilObj, title: str, iconPath: str, size=QSize(200, 200)):
        super().__init__()

        self.__utilObj = utilObj
        self.__size: QSize = size
        self.__title: str = title
        self.__iconPath: str = iconPath

        self.__setDefaultStyle()

    def __setDefaultStyle(self) -> None:
        self.setFixedSize(self.__size)
        self.setStyleSheet("background-color: none; border: none;")
        self.setIconSize(self.__size)
        self.setToolTip(self.__title)
        self.setIcon(QIcon(self.__iconPath))

    def runUtil(self) -> None:
        self.__utilObj.exec()


class TitleLabel(QLabel):
    def __init__(self, text='', size=QSize(375, 50)):
        super().__init__()

        self.__size: QSize = size
        self.__text: str = text

        self.setFixedSize(self.__size)
        self.setStyleSheet("font-weight: bold; font-size: 30px;")
        self.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.setText(self.__text)


class FileSelectButton(QPushButton):
    def __init__(self, size=QSize(200, 200), crossColor="#222222", backgroundColor="#cccccc"):
        super().__init__()

        self.__size: QSize = size
        self.__backgroundColor: str = backgroundColor
        self.__crossColor: str = crossColor

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
        
        self.widget: QWidget = QWidget()
        self.layout: QVBoxLayout = QVBoxLayout()
        self.setFixedSize(750, 500)

        self.label: MenuIcon = MenuIcon(utilObj=TitleLabel("Title Label"), title="Title Label", iconPath="./res/fileSelected.ico")
        self.label.clicked.connect(lambda: print("Clicked")) 
        
        self.layout.addWidget(self.label)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

if __name__ == '__main__':
    app = QApplication([])
    interface = ApplicationGUI()
    interface.show()
    app.exec()
