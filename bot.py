import buff, threading

class Bot:

    thread = None
    stop_threads = False
    
    def __init__(self):
        self.activation_key = "f1"
        self.interval = 2
        self.cycles = 3
        self.buffs = buff.Buff.load_skills()

    def bot_loop(self, stop):
        for i in range(1, self.cycles):
            print("Executing rotation for time", i)
            for skill in self.buffs:
                if stop():
                    break
                skill.cast()
    
    def disable(self):
        if not Bot.thread:
            return
        Bot.stop_threads = True
        Bot.thread.join()

    def multithreading(self):
        if Bot.thread:
            print("bot already running")
            return 
        Bot.stop_threads = False
        Bot.thread = threading.Thread(target = self.bot_loop, args = (lambda : Bot.stop_threads,))
        Bot.thread.start()