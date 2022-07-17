
from PyQt5.QtWidgets import QAction

class SubmenuItem:

    def __init__(self, name, menu, application):
        self.menu = menu
        self.name = name
        self.application = application
        self.command = lambda: get_command()

        def get_command():
            if self.name == "Exit":
                self.command = self.application.app.quit

    def create_action(self):
        q_action = QAction(self.name, self.menu.get_window())
        q_action.triggered.connect(self.command)
        return q_action

