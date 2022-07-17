from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import menuitem

class MainWindow(QMainWindow):

    default_user_agent = "None"
    config_file = "menus.json"

    def __init__(self, properties, application):
        super(MainWindow, self).__init__()
        self.vk_code_map = properties.load_vk_code()
        self.set_app_window_properties(properties)
        self.load_user_agent()
        self.menu = self.load_menu(application)
        self.load_homepage(properties)

    def set_app_window_properties(self, properties):
        window = properties.set_window_properties(self)
        window.browser = None
        window.showNormal()

    def load_user_agent(self):
        return MainWindow.default_user_agent

    def load_homepage(self, properties):
        if not self.browser or self.browser.strip() == "":
            self.browser = None
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl(properties.get_url()))
    
    def load_menu(self, application):
        menu = menuitem.MenuItem(MainWindow.config_file, self, application)
        return menu.add_to_window()
