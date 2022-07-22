import os
import json

import submenuitem, bot, windowproperties

class MenuItem:

    config_file = "menus.json"

    @staticmethod
    def menu_items():
        application_menus = []
        menus_json = os.path.join(windowproperties.WindowProperties.config_directory, MenuItem.config_file)
        with open(menus_json, 'r') as json_file:
            menus = json.load(json_file)
            for menu_json in menus['menus']:
                menu = MenuItem(menu_json['name'], menu_json['submenu'])
                application_menus.append(menu)            
        return application_menus

    def __init__(self, name, submenu_list):
        self.name = name
        self.submenu_items = submenu_list

    def add_to_window(self, window, application):
        menu_bar = window.menuBar().addMenu(self.name)
        return self.populate_submenu(window, menu_bar, application)

    def populate_submenu(self, window, menubar, application):
        for submenu_item in self.submenu_items:
            submenu = submenuitem.SubmenuItem(submenu_item['name'], self.name)
            macro_bot = bot.Bot(window.statusbar)
            menubar.addAction(submenu.create_action(window, application, macro_bot))
        return self
