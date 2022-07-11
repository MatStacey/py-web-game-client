from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Window(QMainWindow):

    default_user_agent = "None"

    def __init__(self, properties, application):
        self.windows = [self]
        super(Window, self).__init__()
        self.vk_code_map = properties.load_vk_code()
        self.set_app_window_properties(properties)
        self.load_user_agent()
        self.load_menu(application)
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
        menu_items = ["File", "Macro", "Settings", "Community", "About"]
        for menu_item in menu_items:
            submenu_item = self.menuBar().addMenu(menu_item)
            if menu_item == "File":

                new_window_action = QAction("New Window", self)
                new_window_action.triggered.connect(lambda: self.new_window())
                submenu_item.addAction(new_window_action)

                exit_action = QAction("Exit", self)
                exit_action.triggered.connect(application.app.quit)
                submenu_item.addAction(exit_action)


    def new_window(self):
        pass