from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
import menuitem
import os

class MainWindow(QMainWindow):

    default_user_agent = "None"
    default_profile = "default"
    profile_folder = str(os.getenv('APPDATA') + "\py-flyff-client\profiles\\" + default_profile)

    def __init__(self, properties, application, name):
        super(MainWindow, self).__init__()
        properties.set_window_properties(self)
        self.app_name = name
        for menu in menuitem.MenuItem.menu_items():
            menu.add_to_window(self, application)

        self.browser = QWebEngineView()

        main_profile = QWebEngineProfile(MainWindow.default_profile, self.browser)
        main_profile.setCachePath(MainWindow.profile_folder)
        main_profile.setPersistentStoragePath(MainWindow.profile_folder)

        main_page = QWebEnginePage(main_profile, self.browser)
        self.browser.setPage(main_page)
        self.setWindowTitle(self.app_name)
        self.setCentralWidget(self.browser)
        self.browser.page().profile().setHttpUserAgent(MainWindow.default_user_agent)
        properties.set_url(self.browser)
        
