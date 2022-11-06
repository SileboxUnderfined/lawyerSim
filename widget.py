from PyQt6.QtWidgets import QWidget, QMainWindow
from PyQt6.uic import loadUi
from resource_path import resource_path as rp
from abc import abstractmethod

class Widget(QWidget):
    def __init__(self,uifile):
        super(Widget, self).__init__()

        self.ui = loadUi(rp(f'ui/{uifile}.ui'), self)
        self.initSignals()
        self.connectButtons()

        self.show()

    @abstractmethod
    def connectButtons(self): pass

    @abstractmethod
    def initSignals(self): pass

class MainWindow(QMainWindow):
    def __init__(self, uifile):
        super(MainWindow, self).__init__()

        self.ui = loadUi(rp(f'ui/{uifile}.ui'), self)

        self.initPages()
        self.addToStack()
        self.connectSignals()

        self.show()

    @abstractmethod
    def initPages(self):
        pass

    @abstractmethod
    def addToStack(self):
        pass

    def connectSignals(self):
        self.stackedWidget.currentChanged.connect(self.widgetChanged)

    def widgetChanged(self):
        print(self.stackedWidget.currentWidget().windowTitle())
        self.setWindowTitle(self.stackedWidget.currentWidget().windowTitle())
