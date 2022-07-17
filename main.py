from PyQt5.QtWidgets import QApplication
import windowproperties, window, sys

class Application(QApplication):

    default_config = 'properties.json'

    def __init__(self, name):
        super(Application).__init__()
        self.setApplicationName(name)
        self.app = QApplication(sys.argv)
        self.window = window.Window(windowproperties.WindowProperties(Application.default_config), self)
    
    def run(self):
        self.app.exec_()

Application("Flyff - Test", ).run()
