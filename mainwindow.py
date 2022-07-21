from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
import menuitem

class MainWindow(QMainWindow):

    default_user_agent = "None"
    profile_folder = "C:/PyFlyffClient/profiles/buttface"
    profile_name = "Default"

    def __init__(self, properties, application, name):
        super(MainWindow, self).__init__()
        window = properties.set_window_properties(self)
        window.browser = None
        window.showNormal()
        self.app_name = name
        self.load_menu(application)
        self.load_homepage(properties)

    def load_homepage(self, properties):
        if not self.browser or self.browser.strip() == "":
            self.browser = None

        self.browser = QWebEngineView()
        main_profile = QWebEngineProfile(MainWindow.profile_name, self.browser)
        main_profile.setCachePath(MainWindow.profile_folder)
        main_profile.setPersistentStoragePath(MainWindow.profile_folder)
        main_page = QWebEnginePage(main_profile, self.browser)
        self.browser.setPage(main_page)

        self.setCentralWidget(self.browser)
        self.browser.setUrl(properties.get_url())
        self.setWindowTitle(self.app_name)
        self.browser.page().profile().setHttpUserAgent(MainWindow.default_user_agent)
    
    def load_menu(self, application):
        for menu in menuitem.MenuItem.menu_items():
            menu.add_to_window(self, application)
