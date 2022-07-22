import skill, threading
import win32gui

class Bot:

    thread = None
    stop_threads = False
    
    def __init__(self, statusbar):
        self.buffs = skill.Skill.load_buffs()
        self.spells = skill.Skill.load_spells()
        self.statusbar = statusbar
        self.window_name = "Flyff Python Client - default"

    def buff_heal(self, stop):
        hwndMain = win32gui.FindWindow(None, self.window_name)
        print("running in window", self.window_name)
        run_loop = True
        counter = 0
        while run_loop:
            print("Executing rotation for time", counter)
            for buff in self.buffs:
                if stop():
                    run_loop = False
                    break
                if buff.has_assigned_hotkey() and not buff.is_active():
                    buff.cast(hwndMain)
                    buff.set_as_active()
            for spell in self.spells:
                if stop():
                    run_loop = False
                    break
                if spell.has_assigned_hotkey():
                    spell.cast(hwndMain)
                    spell.reduce_cast_rate()
            if stop():
                skill.Skill.reset_buffs(self.buffs)
                run_loop = False
            counter += 1     

    def heal(self, stop):
        hwndMain = win32gui.FindWindow(None, self.window_name)
        run_loop = True
        counter = 0
        while run_loop:
            for spell in self.spells:
                if spell.has_assigned_hotkey():
                    spell.cast(hwndMain)
                    spell.reduce_cast_rate()
            if stop():
                skill.Skill.reset_buffs(self.buffs)
                run_loop = False
            counter += 1
        

    def buff(self, stop):
        hwndMain = win32gui.FindWindow(None, self.window_name)
        run_loop = True
        for buff in self.buffs:
            if not run_loop:
                break
            if buff.has_assigned_hotkey() and not buff.is_active():
                buff.cast(hwndMain)
                buff.set_as_active()
            if stop():
                run_loop = False
        skill.Skill.reset_buffs(self.buffs)
        self.disable()     

    def disable(self):
        if not Bot.thread:
            return
        Bot.stop_threads = True
        Bot.thread = None

    def multithreading(self, profile):
        print("profile = ", profile)
        if Bot.thread:
            self.statusbar.showMessage("Macro Already Running", 3000)
            return 
        self.window_name = "Flyff Python Client" + " - " + profile
        self.statusbar.showMessage("Running Buff & Heal Macro for " + profile + " profile", 6000) 
        Bot.stop_threads = False
        Bot.thread = threading.Thread(target = self.buff_heal, args = (lambda : Bot.stop_threads,))
        Bot.thread.start()

    def multithreading_heal(self, profile):
        if Bot.thread:
            self.statusbar.showMessage("Macro Already Running", 3000)
            return 
        self.window_name = "Flyff Python Client" + " - " + profile
        self.statusbar.showMessage("Running Heal Macro for " + profile + " profile", 6000)
        Bot.stop_threads = False
        Bot.thread = threading.Thread(target = self.heal, args = (lambda : Bot.stop_threads,))
        Bot.thread.start()

    def multithreading_buff(self, profile):
        if Bot.thread:
            self.statusbar.showMessage("Macro Already Running", 3000)
            return  
        self.window_name = "Flyff Python Client" + " - " + profile
        self.statusbar.showMessage("Running Buff Macro for " + profile + " profile", 6000)
        Bot.stop_threads = False
        Bot.thread = threading.Thread(target = self.buff, args = (lambda : Bot.stop_threads,))
        Bot.thread.start()
        