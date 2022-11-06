from PyQt6.QtCore import QObject, pyqtSignal

class mainMenuSignals:
    class toStart(QObject): goto = pyqtSignal()
    class toLoad(QObject): goto = pyqtSignal()
    class toAbout(QObject): goto = pyqtSignal()
    class toSettings(QObject): goto = pyqtSignal()
    class toBack(QObject): goto = pyqtSignal()

class startSignals:
    class toBack(QObject): goto = pyqtSignal()
    class toGame(QObject): goto = pyqtSignal()

class loadSignals:
    class toBack(QObject): goto = pyqtSignal()
    class toGame(QObject): goto = pyqtSignal()

class aboutSignals:
    class toBack(QObject): goto = pyqtSignal()