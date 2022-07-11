from PyQt5.QtWidgets import QApplication

import windowproperties, window, sys

class Application(QApplication):

    def __init__(self, name):
        super(Application).__init__()
        self.setApplicationName(name)
        self.app = QApplication(sys.argv)
        self.app_properties = windowproperties.WindowProperties(windowproperties.WindowProperties.flyff_url)
        self.window = window.Window(self.app_properties, self)
    
    def run(self):
        self.app.exec_()

Application("Flyff", ).run()
