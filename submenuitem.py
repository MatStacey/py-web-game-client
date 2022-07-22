
from PyQt5.QtWidgets import QAction

class SubmenuItem:

    def __init__(self, name, menu_name):
        self.menu_name = menu_name.lower()
        self.name = name.lower()
        self.modifier = "Ctrl"

    # MMM Janky if statements with hardcoded strings > will sort out later (maybe. if i can be bothered)
    def create_action(self, window, application, macro):
        q_action = QAction(self.name.title(), window)
        if self.menu_name == "file":
            if(self.name == "new window"):
                q_action.setShortcut(self.modifier + "+N")
                q_action.triggered.connect(lambda: application.create_alt_window())
            elif(self.name == "exit"):
                q_action.triggered.connect(lambda: application.quit(macro))
        elif self.menu_name == "run":
            if self.name == "buff & heal":
                q_action.setShortcut(self.modifier + "+1")
                q_action.triggered.connect(lambda: macro.multithreading())
            elif self.name == "buff":
                q_action.setShortcut(self.modifier + "+2")
                q_action.triggered.connect(lambda: macro.multithreading_buff())
            elif self.name == "heal":
                q_action.setShortcut(self.modifier + "+3")
                q_action.triggered.connect(lambda: macro.multithreading_heal())
            elif self.name == "stop":
                q_action.setShortcut(self.modifier + "+C")
                q_action.triggered.connect(lambda: macro.disable())
        return q_action
    
