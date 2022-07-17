
from PyQt5.QtWidgets import QAction

class SubmenuItem:

    def __init__(self, name, menu, application):
        self.menu = menu
        self.name = name
        self.application = application
        self.command = None

    def create_action(self):
        q_action = QAction(self.name, self.menu.get_window())
        if(self.name == "Exit"):
            q_action.triggered.connect(self.application.app.quit)
        return q_action

