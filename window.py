from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Window(QMainWindow):

    default_user_agent = "None"

    def __init__(self, properties, application):
        super(Window, self).__init__()
        self.vk_code_map = properties.load_vk_code()
        self.set_main_window_properties(properties)
        self.load_user_agent()
        self.load_menu(application)
        self.load_flyff_homepage(properties)

    def set_main_window_properties(self, properties):
        window = properties.set_window_properties(self)
        window.showMaximized()

    def load_user_agent(self):
        return Window.default_user_agent

    def load_flyff_homepage(self, properties):
        if not self.browser or self.browser.strip() == "":
            self.browser = None
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl(properties.get_url()))
    
    def load_menu(self, application):
        menu_items = ["File", "Macro", "Settings", "Community", "About"]
        for menu_item in menu_items:
            submenu_item = self.menuBar().addMenu(menu_item)
            if menu_item == "File":
                exit = QAction("Exit", self)
                exit.triggered.connect(application.app.quit)
                submenu_item.addAction(exit)