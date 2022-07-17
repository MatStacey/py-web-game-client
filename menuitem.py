import submenuitem

class MenuItem:

    def __init__(self, name, window, application):
        self.name = name
        self.window = window
        self.application = application
        self.menubar = None
        self.submenu_items = ["Exit", "Macro"]


    def add_to_window(self):
        self.menubar = self.window.menuBar().addMenu(self.name)
        self.populate_submenu()
        return self

    def get_window(self):
        return self.window

    def populate_submenu(self):
        for submenu_item in self.submenu_items:
            submenu = submenuitem.SubmenuItem(submenu_item, self)
            self.menubar.addAction(submenu.create_action())
        return self
