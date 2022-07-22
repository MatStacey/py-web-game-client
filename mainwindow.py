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
        properties.set_window_icon(self)
        self.setMinimumSize(640, 480)
        self.app_name = name

        for menu in menuitem.MenuItem.menu_items():
            menu.add_to_window(self, application)

        self.browser = QWebEngineView()
        self.browser.setPage(QWebEnginePage(properties.get_profile(self.browser), self.browser))
        properties.set_profile_user_agent(self.browser.page().profile())
        self.setWindowTitle(self.app_name)
        self.setCentralWidget(self.browser)
        properties.set_url(self.browser)
        self.showMaximized()
        
