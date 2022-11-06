from widget import Widget
from signals import loadSignals as ls
import os, os.path, json

class Load(Widget):
    def __init__(self):
        super(Load, self).__init__('load')

        self.selectFile_comboBox.addItems(os.listdir('saves'))

    def initSignals(self):
        self.toBack = ls.toBack()
        self.toGame = ls.toGame()

    def connectButtons(self):
        self.back_Button.clicked.connect(self.toBack.goto.emit)
        self.load_Button.clicked.connect(self.loadGame)

    def loadGame(self):
        with open(os.path.join('saves',self.selectFile_comboBox.currentText()),'rt') as f:
            self.data = json.load(f)
            print(self.data)

        self.toGame.goto.emit()

if __name__ in "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = Load()
    app.exec()