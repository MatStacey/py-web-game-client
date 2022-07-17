from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import menuitem


class Window(QMainWindow):

    default_user_agent = "None"

    def __init__(self, properties, application):
        # self.windows = [self]
        super(Window, self).__init__()
        self.vk_code_map = properties.load_vk_code()
        self.set_app_window_properties(properties)
        self.load_user_agent()
        self.menu = self.load_menu(application)
        self.load_homepage(properties)

    def set_app_window_properties(self, properties):
        window = properties.set_window_properties(self)
        window.browser = None
        window.showMaximized()

    def load_user_agent(self):
        return Window.default_user_agent

    def load_homepage(self, properties):
        if not self.browser or self.browser.strip() == "":
            self.browser = None
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl(properties.get_url()))
    
    def load_menu(self, application):
        menu = menuitem.MenuItem("File", self, application)
        return menu.add_to_window()
