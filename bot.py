import buff
import win32gui
import win32con
import win32api
import random, time

class Bot:
    
    def __init__(self):
        self.activation_key = "f1"
        self.interval = 2
        self.cycles = 3
        self.buffs = buff.Buff.load_skills()
        self.activated = False
    
    def is_activated(self):
        return self.activated

    def toggle(self):
        self.activated = not self.activated

    @staticmethod
    def bot_loop(bot):
        if bot.is_activated():
            try:
                for i in range(0, bot.cycles):
                    print("Executing rotation for time", i)
                # while counter < bot.cycles:
                #     for buff in bot.buffs:
                    for buff in bot.buffs:
                        buff.cast()
                        # win32api.SendMessage(window, win32con.WM_KEYDOWN, i, 0)
                        # time.sleep(random.uniform(0.369420, 0.769420))
                        # win32api.SendMessage(window, win32con.WM_KEYUP, bot.activation_key, 0)

            except Exception as e:
                print(e)

Bot.bot_loop(Bot())
