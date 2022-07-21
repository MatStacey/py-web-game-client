import skill, threading
import win32gui

class Bot:

    thread = None
    stop_threads = False
    
    def __init__(self):
        self.buffs = skill.Skill.load_buffs()
        self.spells = skill.Skill.load_spells()

    def buff_heal(self, stop):
        hwndMain = win32gui.GetForegroundWindow()
        run_loop = True
        counter = 0
        while run_loop:
            print("Executing rotation for time", counter)
            for buff in self.buffs:
                if stop():
                    break
                if buff.has_assigned_hotkey() and not buff.is_active():
                    buff.cast(hwndMain)
                    buff.set_as_active()
            for spell in self.spells:
                if stop():
                    break
                if spell.has_assigned_hotkey():
                    spell.cast(hwndMain)
                    spell.reduce_cast_rate()
            if stop():
                print("Macro stopped")
                skill.Skill.reset_buffs(self.buffs)
                run_loop = False
            counter += 1

    def heal(self, stop):
        hwndMain = win32gui.GetForegroundWindow()
        run_loop = True
        counter = 0
        while run_loop:
            print("Healing", counter)
            for spell in self.spells:
                if spell.has_assigned_hotkey():
                    spell.cast(hwndMain)
                    spell.reduce_cast_rate()
            if stop():
                print("Bot stopped")
                skill.Skill.reset_buffs(self.buffs)
                run_loop = False
            counter += 1
        

    def buff(self, stop):
        hwndMain = win32gui.GetForegroundWindow()
        print("buffing target")
        run_loop = True
        for buff in self.buffs:
            if not run_loop:
                break
            if buff.has_assigned_hotkey() and not buff.is_active():
                buff.cast(hwndMain)
                buff.set_as_active()
            if stop():
                print("Macro stopped")
                run_loop = False
        skill.Skill.reset_buffs(self.buffs)
        self.disable()        

    def disable(self):
        if not Bot.thread:
            return
        Bot.stop_threads = True
        Bot.thread = None

    def multithreading(self):
        if Bot.thread:
            print("Macro already running")
            return 
        Bot.stop_threads = False
        Bot.thread = threading.Thread(target = self.buff_heal, args = (lambda : Bot.stop_threads,))
        Bot.thread.start()

    def multithreading_heal(self):
        if Bot.thread:
            print("Macro already running")
            return 
        Bot.stop_threads = False
        Bot.thread = threading.Thread(target = self.heal, args = (lambda : Bot.stop_threads,))
        Bot.thread.start()

    def multithreading_buff(self):
        if Bot.thread:
            print("Macro already running")
            return 
        Bot.stop_threads = False
        Bot.thread = threading.Thread(target = self.buff, args = (lambda : Bot.stop_threads,))
        Bot.thread.start()
        