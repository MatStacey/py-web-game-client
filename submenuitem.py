
from PyQt5.QtWidgets import QAction
import bot
import threading

class SubmenuItem:

    def __init__(self, name, menu, application):
        self.menu = menu
        self.name = name
        self.application = application

    # MMM Janky if statements with hardcoded strings > will sort out later
    def create_action(self):
        q_action = QAction(self.name, self.menu.get_window())
        if(self.name == "Exit"):
            q_action.triggered.connect(self.application.app.quit)
        if(self.name == "New Window"):
            q_action.triggered.connect(lambda: self.application.create_alt_window())
        if(self.name == "Macro"):
            window = self.menu.get_window()
            buff_bot = bot.Bot()
            buff_bot.toggle()
            q_action.triggered.connect(lambda: window.multithreading(bot.Bot.bot_loop(buff_bot)))
        return q_action

