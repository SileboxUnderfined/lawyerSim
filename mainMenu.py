from widget import Widget
from PyQt6.QtCore import QCoreApplication
from signals import mainMenuSignals as mms

class MainMenu(Widget):
    def __init__(self):
        super(MainMenu, self).__init__('mainMenu')

    def initSignals(self):
        self.toAbout = mms.toAbout()
        self.toStart = mms.toStart()
        self.toLoad = mms.toLoad()
        self.toSettings = mms.toSettings()

    def connectButtons(self):
        self.start_Button.clicked.connect(self.toStart.goto.emit)
        self.about_Button.clicked.connect(self.toAbout.goto.emit)
        self.load_Button.clicked.connect(self.toLoad.goto.emit)
        self.settings_Button.clicked.connect(self.toSettings.goto.emit)
        self.exit_Button.clicked.connect(lambda: QCoreApplication.quit())

if __name__ in "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = MainMenu()
    app.exec()