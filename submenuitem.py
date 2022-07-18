
from PyQt5.QtWidgets import QAction
import bot

class SubmenuItem:

    def __init__(self, name, menu, application):
        self.menu = menu
        self.name = name
        self.application = application
        self.buff_bot = None


    # MMM Janky if statements with hardcoded strings > will sort out later
    def create_action(self):
        q_action = QAction(self.name, self.menu.get_window())
        self.buff_bot = bot.Bot(self.menu.get_window())
        if(self.name == "Exit"):
            q_action.triggered.connect(self.application.app.quit)
        elif(self.name == "New Window"):
            q_action.triggered.connect(lambda: self.application.create_alt_window())
        elif(self.name == "Start Macro"):
            q_action.triggered.connect(lambda: self.buff_bot.multithreading())
        elif(self.name == "Stop Macro"):
            q_action.triggered.connect(lambda: self.buff_bot.disable())
        return q_action
    
