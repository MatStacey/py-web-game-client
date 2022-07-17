import submenuitem
import os
import windowproperties
import json

class MenuItem:

    def __init__(self, file, window, application):
        menus_json = os.path.join(windowproperties.WindowProperties.config_directory, file)
        self.window = window
        self.application = application
        self.menubar = None
        with open(menus_json, 'r') as json_file:
            menus = json.load(json_file)
            self.name = menus['name']
            self.submenu_names = menus['submenu']


    def add_to_window(self):
        self.menubar = self.window.menuBar().addMenu(self.name)
        self.populate_submenu()
        return self

    def get_window(self):
        return self.window

    def populate_submenu(self):
        for submenu_item in self.submenu_names:
            submenu = submenuitem.SubmenuItem(submenu_item['name'], self, self.application)
            self.menubar.addAction(submenu.create_action())
        return self
