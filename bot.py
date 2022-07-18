import buff, threading
import win32gui

class Bot:

    thread = None
    stop_threads = False
    
    def __init__(self, window):
        self.activation_key = "f1"
        self.interval = 2
        self.cycles = 10
        self.buffs = buff.Buff.load_skills()
        self.window = window

    def bot_loop(self, stop):
        hwndMain = win32gui.GetForegroundWindow()
        run_loop = True
        counter = 0
        while run_loop:
            print("Executing rotation for time", counter)
            for skill in self.buffs:
                if stop():
                    run_loop = False
                skill.cast(self.window, hwndMain)
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
        