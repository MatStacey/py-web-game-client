from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
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
        self.name = properties.get_app_name()

    def get_vk_code_map(self):
        return self.vk_code_map

    def get_name(self):
        return self.name

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

        client_folder = "C:/PyFlyffClient/profiles/profile"

        main_profile = QWebEngineProfile("profile", self.browser)
        main_profile.setCachePath(client_folder)
        main_profile.setPersistentStoragePath(client_folder)
        main_page = QWebEnginePage(main_profile, self.browser)

        self.browser.setPage(main_page)

        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl(properties.get_url()))
        self.setWindowTitle("Flyff - Test")
        self.browser.page().profile().setHttpUserAgent(self.load_user_agent())
    
    def load_menu(self, application):
        menu = menuitem.MenuItem(MainWindow.config_file, self, application)
        return menu.add_to_window()
