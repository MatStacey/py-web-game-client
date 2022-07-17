# from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon
import mainwindow, windowproperties

class AltWindow(QWebEngineView):

    #Look ok, i know this sucks, its on the list
    def __init__(self):
        super().__init__()
        self.windows = []
        properties = windowproperties.WindowProperties('properties.json')
        self.setAttribute(Qt.WA_DeleteOnClose)

        #I don't understand why i need to create an arbitrary list but if it stops it exploding then ok
        self.destroyed.connect(lambda: self.windows.remove(self))

        alt_page = QWebEnginePage(QWebEngineProfile(properties.get_name(), self), self)
        self.setPage(alt_page)
        self.load(QUrl(properties.get_url()))
        self.setWindowTitle(properties.get_name())
        self = properties.set_window_properties(self)
        self.showNormal()
        self.page().profile().setHttpUserAgent(mainwindow.MainWindow.default_user_agent)
        self.windows.append(self)
        
