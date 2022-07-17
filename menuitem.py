import submenuitem

class MenuItem:

    def __init__(self, name, window, application):
        self.name = name
        self.window = window
        self.application = application
        self.menubar = None

    def add_to_window(self):
        self.menubar = self.window.menuBar().addMenu(self.name)
        self.populate_submenu(["Exit"])
        return self

    def get_window(self):
        return self.window

    def populate_submenu(self, items):
        for submenu_item in items:
            submenu = submenuitem.SubmenuItem(submenu_item, self)
            self.menubar.addAction(submenu.create_action(self.application.app.quit))
        return self
