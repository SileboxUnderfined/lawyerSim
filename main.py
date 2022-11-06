from PyQt6.QtWidgets import QApplication
from mainMenu import MainMenu
from start import Start
from widget import MainWindow
import sys

class Main(MainWindow):
    def __init__(self):
        super(Main, self).__init__('main')

        self.stackedWidget.setCurrentWidget(self.mm)
        #self.setWindowTitle(self.mm.windowTitle())

    def initPages(self):
        self.mm = MainMenu()
        self.start = Start()

    def addToStack(self):
        self.stackedWidget.addWidget(self.mm)
        self.stackedWidget.addWidget(self.start)

    def connectSignals(self):
        self.mm.toStart.goto.connect(lambda: self.stackedWidget.setCurrentWidget(self.start))
        self.start.toBack.goto.connect(lambda: self.stackedWidget.setCurrentWidget(self.mm))

if __name__ in "__main__":
    app = QApplication(sys.argv)
    window = Main()
    app.exec()