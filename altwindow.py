# from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon
import mainwindow, windowproperties

class AltWindow(QWebEngineView):

    def __init__(self, properties, application):
        super().__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.destroyed.connect(lambda: application.unregister_alt_window(self))
        properties.load_alt_profile(self)
        properties.set_profile_user_agent(self.page().profile())
        properties.set_alt_window_title(self, application.applicationName())
        application.register_alt_window(self)
        self.showNormal()
        
