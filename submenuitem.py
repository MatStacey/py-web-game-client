
from PyQt5.QtWidgets import QAction

class SubmenuItem:

    def __init__(self, name, menu_name):
        self.menu_name = menu_name.lower()
        self.name = name.lower()

    # MMM Janky if statements with hardcoded strings > will sort out later
    def create_action(self, window, application, macro):
        q_action = QAction(self.name, window)
        print("adding menu item", self.name, "to menu", self.menu_name)
        if self.menu_name == "file":
            if(self.name == "new window"):
                q_action.triggered.connect(lambda: application.create_alt_window())
            elif(self.name == "exit"):
                q_action.triggered.connect(application.app.quit)
        elif self.menu_name == "run":
            if self.name == "buff & heal":
                q_action.triggered.connect(lambda: macro.multithreading())
            elif self.name == "stop":
                q_action.triggered.connect(lambda: macro.disable())
        return q_action
    
