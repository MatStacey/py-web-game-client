import buff, threading
import win32gui

class Bot:

    thread = None
    stop_threads = False
    
    def __init__(self):
        self.activation_key = "f1"
        self.interval = 2
        self.cycles = 10
        self.buffs = buff.Buff.load_skills()

    def bot_loop(self, stop):
        hwndMain = win32gui.GetForegroundWindow()
        run_loop = True
        counter = 0
        while run_loop:
            print("Executing rotation for time", counter)
            for skill in self.buffs:
                if skill.has_assigned_hotkey() and not skill.is_still_active():

                    skill.cast_buff(hwndMain)
                
                    #remove this logic when buffs and spells are split into their own objects
                    if len(buff.Buff.active_buffs) == 9:
                        skill.reduce_cast_rate()
                    if skill.name not in buff.Buff.spells:
                        skill.trigger_cooldown()
            if stop():
                print("Bot stopped")
                buff.Buff.clear_cooldowns(self.buffs)
                buff.Buff.active_buffs = []
                run_loop = False
            counter += 1
    
    def disable(self):
        if not Bot.thread:
            return
        print("Stopping thread")
        Bot.stop_threads = True
        Bot.thread = None

    def multithreading(self):
        if Bot.thread:
            print("bot already running")
            return 
        Bot.stop_threads = False
        Bot.thread = threading.Thread(target = self.bot_loop, args = (lambda : Bot.stop_threads,))
        Bot.thread.start()
        