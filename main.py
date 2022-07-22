from PyQt5.QtWidgets import QApplication
import windowproperties, mainwindow, sys
import altwindow
class Application(QApplication):

    application_name = "Flyff Python Client"

    def __init__(self, name):
        super(Application).__init__()
        self.setApplicationName(name)
        self.app = QApplication(sys.argv)
        properties = windowproperties.WindowProperties.load_from_json(windowproperties.WindowProperties.config)
        self.window = mainwindow.MainWindow(properties, self, self.applicationName())
        self.windows = [self.window]
        self.alt_window = None
    
    def run(self):
        self.app.exec_()

    def create_alt_window(self):
        self.alt_window = altwindow.AltWindow()
        self.alt_window.show()

    def quit(self):
        self.window.browser.page().deleteLater()
        self.app.quit()

Application(Application.application_name, ).run()
