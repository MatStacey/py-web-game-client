from multiprocessing.connection import Client
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

import clientproperties, sys

class MainWindow(QMainWindow):

    default_user_agent = "None"

    def __init__(self, props):
        super(MainWindow, self).__init__()
        self.properties = props
        self.vk_code_map = props.load_vk_code()
        self.set_main_window_properties(self.properties)
        self.load_user_agent()
        self.load_menu()
        self.load_flyff_homepage(self.properties)

    def set_main_window_properties(self, props):
        window = props.set_window_properties(self)
        window.showMaximized()

    def load_user_agent(self):
        return MainWindow.default_user_agent

    def load_flyff_homepage(self, properties):
        if not self.browser or self.browser.strip() == "":
            self.browser = None
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl(properties.get_url()))
    
    def load_menu(self):
        menu_items = ["File", "Macro", "Settings", "Community", "About"]
        for menu_item in menu_items:
            submenu_item = self.menuBar().addMenu(menu_item)
            if menu_item == "File":
                exit = QAction("Exit", self)
                exit.triggered.connect(app.quit)
                submenu_item.addAction(exit)

app = QApplication(sys.argv)
app_properties = clientproperties.ClientProperties(clientproperties.ClientProperties.flyff_url)
QApplication.setApplicationName(app_properties.get_name())
window = MainWindow(app_properties)
app.exec_()
