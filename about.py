from widget import Widget
from signals import aboutSignals
import webbrowser, os.path

class About(Widget):
    def __init__(self):
        super(About, self).__init__('about')

    def initSignals(self):
        self.toBack = aboutSignals.toBack()

    def connectButtons(self):
        self.back_Button.clicked.connect(self.toBack.goto.emit)
        self.github_Button.clicked.connect(lambda: webbrowser.open_new_tab('https://www.github.com/'))
        self.vk_Button.clicked.connect(lambda: webbrowser.open_new_tab('https://vk.com/silentbox1488'))
        self.license_Button.clicked.connect(lambda: webbrowser.open_new_tab('file://' + os.path.realpath('LICENSE')))

if __name__ in "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = About()
    app.exec()