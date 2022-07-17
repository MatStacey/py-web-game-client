from PyQt5.QtWidgets import QApplication
import windowproperties, mainwindow, sys
import altwindow
class Application(QApplication):

    default_config = 'properties.json'

    def __init__(self, name):
        super(Application).__init__()
        self.setApplicationName(name)
        self.app = QApplication(sys.argv)
        self.window = mainwindow.MainWindow(windowproperties.WindowProperties(Application.default_config), self)
        self.windows = [self.window]
        self.alt_window = None
    
    def run(self):
        self.app.exec_()

    def create_alt_window(self):
        self.alt_window = altwindow.AltWindow()
        self.alt_window.show()

Application("Flyff - Test", ).run()
