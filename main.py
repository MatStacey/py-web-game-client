import json,sys, os

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

class ApplicationProperties():
    def __init__(self):
        self.url = "https://universe.flyff.com/play"
        self.app_name = "pyFlyffClient"
        self.icon_file = "icons/PyFlyff.ico"

    def get_name(self):
        return self.app_name

    def get_url(self):
        return self.url

    def get_icon(self):
        return self.icon_file

    def load_vk_code(self):
        config_directory = os.path.dirname(__file__) + '/config'
        vk_code_json_path = os.path.join(config_directory, 'vk_code.json')
        with open(vk_code_json_path, 'r') as json_file:
            vk_code_map = json.load(json_file)
        return vk_code_map

class MainWindow(QMainWindow):

    min_window_size = { "width" : 640, "height" : 480 }
    default_user_agent = "None"

    def __init__(self, properties):
        super(MainWindow, self).__init__()
        self.set_main_window_properties(properties)
        self.vk_code_map = properties.load_vk_code()
        self.load_user_agent()
        self.load_menu()

        self.load_flyff_homepage()
        return

    def set_main_window_properties(self, properties):
        self.browser = None
        self.setWindowIcon(QIcon(properties.get_icon()))
        self.setMinimumSize(MainWindow.min_window_size['width'], MainWindow.min_window_size['height'])
        self.showMaximized()
    
    def load_user_agent(self):
        return MainWindow.default_user_agent

    def load_flyff_homepage(self):
        if not self.browser or self.browser.strip() == "":
            self.browser = None

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl(properties.get_url()))
    
    def load_menu(self):
        menu_items = ["File", "Macro", "Settings", "Community", "About"]
        for menu_item in menu_items:
            self.menuBar().addMenu(menu_item)


app = QApplication(sys.argv)
properties = ApplicationProperties()
QApplication.setApplicationName(properties.get_name())
window = MainWindow(properties)
app.exec_()
