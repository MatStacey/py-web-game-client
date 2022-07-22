from PyQt5.QtWidgets import QApplication
import windowproperties, mainwindow, sys
import altwindow, bot
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
        self.alt_window = altwindow.AltWindow(windowproperties.WindowProperties.load_from_json(windowproperties.WindowProperties.config), self)
        self.alt_window.show()

    def quit(self):
        bot.Bot.thread = None
        bot.Bot.stop_threads = True
        self.window.browser.page().deleteLater()
        self.app.quit()

    def register_alt_window(self, window):
        self.windows.append(window)
    
    def unregister_alt_window(self, window):
        self.windows.remove(window)

Application(Application.application_name, ).run()
