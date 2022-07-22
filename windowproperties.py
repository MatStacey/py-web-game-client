from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
import json, os
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEnginePage

class WindowProperties():

    protocol = "https://"
    config_directory = os.path.dirname(__file__) + "/config"
    profile_folder = os.getenv('APPDATA') + "\py-flyff-client\profiles\\"
    config = "properties.json"

    @staticmethod
    def load_from_json(file):
        window_properties_json = os.path.join(WindowProperties.config_directory, file)
        with open(window_properties_json, 'r') as json_file:
            properties = json.load(json_file)
            return WindowProperties(properties['name'], properties['icon'], properties['default_window_size'], properties['url'], properties['profile'], properties['alt_profile'], properties['user_agent'])

    def __init__(self, name, icon, size, url, profile, alt_profile,user_agent):
        self.app_name = name
        self.icon_file = icon
        self.min_window_size = size
        self.url = url
        self.profile = profile
        self.alt_profile = alt_profile
        self.user_agent = user_agent

    def set_url(self, browser):
        return browser.setUrl(QUrl(WindowProperties.protocol + self.url))
    
    def set_alt_window_title(self, window, name):
        return window.setWindowTitle(name + " - " + self.alt_profile)

    def set_window_title(self, window):
        return window.setWindowTitle(window.app_name + " - " + self.profile)

    def get_profile(self, browser):
        main_profile = QWebEngineProfile(self.profile, browser)
        main_profile.setCachePath(WindowProperties.profile_folder)
        main_profile.setPersistentStoragePath(WindowProperties.profile_folder)
        return main_profile
    
    def load_alt_profile(self, alt_window):
        alt_profile = QWebEngineProfile(self.alt_profile, alt_window)
        alt_window.setPage(QWebEnginePage(alt_profile))
        alt_window.load(QUrl(WindowProperties.protocol + self.url))
        alt_window.setWindowTitle(self.alt_profile)
        alt_window.setWindowIcon(QIcon(self.icon_file))
        alt_window.page().profile().setHttpUserAgent(self.user_agent)
        return alt_window

    def set_profile_user_agent(self, profile):
        profile.setHttpUserAgent(self.user_agent)
        return profile

    def set_window_icon(self, window):
        window.setWindowIcon(QIcon(self.icon_file))
        return window
