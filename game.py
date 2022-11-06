from widget import MainWindow

class Game(MainWindow):
    def __init__(self):
        super(Game, self).__init__('main')
        super(Game, self).connectSignals()


    def initPages(self):
        pass

    def addToStack(self):
        pass

    def connectSignals(self):
        pass

def startGame():
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = Game
    app.exec()

if __name__ in "__main__":
    startGame()