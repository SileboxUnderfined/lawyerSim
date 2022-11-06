from widget import Widget
from signals import startSignals as ss
import os, os.path, json

class Start(Widget):
    def __init__(self):
        super(Start, self).__init__('start')

        self.start_Button.setEnabled(False)

    def initSignals(self):
        self.toBack = ss.toBack()
        self.toGame = ss.toGame()

        self.name_Input.textChanged.connect(self.activateGameButton)
        self.surname_Input.textChanged.connect(self.activateGameButton)
        self.filename_Input.textChanged.connect(self.activateGameButton)

    def connectButtons(self):
        self.back_Button.clicked.connect(self.toBack.goto.emit)
        self.start_Button.clicked.connect(self.startGame)

    def startGame(self):
        if not os.path.isdir('saves'): os.mkdir('saves')

        with open(os.path.join('saves',f"{self.filename_Input.text()}.json"),'wt') as f:
            data = {
                'name':self.name_Input.text(),
                'surname':self.surname_Input.text(),
                'birthDate':self.birth_DateEdit.date().toString('MMMM d, yyyy'),
                'specialization':self.specialization_ComboBox.currentText()
            }
            json.dump(data, f)

    def activateGameButton(self):
        if self.name_Input.text() != "" and self.surname_Input.text() != "" and self.filename_Input.text() != "":
            self.start_Button.setEnabled(True)
        else: self.start_Button.setEnabled(False)

if __name__ in "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = Start()
    app.exec()