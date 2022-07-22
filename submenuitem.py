
from PyQt5.QtWidgets import QAction

class SubmenuItem:

    profile = "default"

    def __init__(self, name, menu_name):
        self.menu_name = menu_name.lower()
        self.name = name.lower()
        self.modifier = "Ctrl"
        self.profile = "default"

    # MMM Janky if statements with hardcoded strings > will sort out later (maybe. if i can be bothered)
    def create_action(self, window, application, macro):
        q_action = QAction(self.name.title(), window)
        if self.menu_name == "file":
            if self.name == "new window":
                q_action.setShortcut(self.modifier + "+N")
                q_action.triggered.connect(lambda: application.create_alt_window())
            elif self.name == "exit":
                q_action.triggered.connect(lambda: application.quit(macro))
        elif self.menu_name == "run":
            if self.name == "buff & heal":
                q_action.setShortcut(self.modifier + "+Q")
                q_action.triggered.connect(lambda: macro.multithreading(SubmenuItem.profile))
            elif self.name == "buff":
                q_action.setShortcut(self.modifier + "+W")
                q_action.triggered.connect(lambda: macro.multithreading_buff(SubmenuItem.profile))
            elif self.name == "heal":
                q_action.setShortcut(self.modifier + "+E")
                q_action.triggered.connect(lambda: macro.multithreading_heal(SubmenuItem.profile))
            elif self.name == "stop":
                q_action.setShortcut(self.modifier + "+R")
                q_action.triggered.connect(lambda: macro.disable())
        elif self.menu_name == "settings":
            if self.name == "run in main window":
                q_action.setShortcut(self.modifier + "+Z")
                q_action.triggered.connect(lambda: SubmenuItem.change_profile("default"))
            elif self.name == "run in alt window":
                q_action.setShortcut(self.modifier + "+X")
                q_action.triggered.connect(lambda: SubmenuItem.change_profile("alt"))
        return q_action
    
    @staticmethod
    def change_profile(name):
        SubmenuItem.profile = name
