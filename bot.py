import buff
import win32gui
import win32con
import win32api
import random, time

class Bot:
    
    def __init__(self):
        self.activation_key = "f1"
        self.interval = 2
        self.cycles = 1
        self.buffs = buff.Buff.load_skills()
    
    @staticmethod
    def bot_loop(bot):
        try:
            for i in range(0, bot.cycles):
                for buff in bot.buffs:
                    print("test:" + str(buff) )
                    # win32api.SendMessage(window, win32con.WM_KEYDOWN, i, 0)
                    # time.sleep(random.uniform(0.369420, 0.769420))
                    # win32api.SendMessage(window, win32con.WM_KEYUP, bot.activation_key, 0)

        except Exception as e:
            print("Error")

Bot.bot_loop(Bot())
