
from PyQt5.QtWidgets import QAction

class SubmenuItem:

    def __init__(self, name, menu):
        self.menu = menu
        self.name = name

    def create_action(self, action):
        q_action = QAction(self.name, self.menu.get_window())
        q_action.triggered.connect(action)
        return q_action