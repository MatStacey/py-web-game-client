import windowproperties, os, json
import random, time
from datetime import datetime, timedelta
import win32gui
import win32con
import win32api
import mainwindow

class Buff:

    skills_json_file = 'skills.json'
    random_min = 0.37448262
    random_max = 0.58573920
    active_buffs = []

    def __init__(self, skill):
        self.name = skill['name']
        self.cool_down = skill['cool_down']
        self.hotkey_input = str(skill['hotkey']).lower()
        self.base_value = skill['base_value']
        self.int_scaling = skill['int_scaling']
        self.cast_time = skill['cast_time']
        self.level = skill['level']
        self.max_level = skill['max_level']
        self.scales_on = skill['scales_on']
        self.tier = skill['tier']
        self.job = skill['job']
        self.on_cooldown = False
        self.cooldown_started = ""
        self.buff_cooldown_expiration = 0

    def get_name(self):
        return self.name

    def get_hotkey_value(self, code_map):
        return int(code_map.get(self.hotkey_input), 16)

    def cast(self, window, hwndMain):
        try:
            if self.hotkey_input == None or self.hotkey_input == "" or self.hotkey_input == "none":
                return

            int_value = 213
            if self.name not in ["heal", "holy_cross"] and self.cooldown_started != "" and len(Buff.active_buffs) > 0:
                if(datetime.now() < self.buff_cooldown_expiration):
                    print("[", datetime.now(), "]", "Not Casting Buff", self.name, ". Still active until time", self.buff_cooldown_expiration)
                    return
                Buff.active_buffs.remove(self)

            hotkey_value = self.get_hotkey_value(window.get_vk_code_map())            
            
            print("[", datetime.now(), "]", "Casting Buff:", self.name, self.cool_down, self.base_value, self.int_scaling, self.cast_time, self.level, self.max_level, self.scales_on, self.tier, self.job)
            win32api.SendMessage(hwndMain, win32con.WM_KEYDOWN, hotkey_value, 0)
            time.sleep(random.uniform(random.uniform(0.39572048,0.58236452), random.uniform(0.626483, 0.8448473)))
            win32api.SendMessage(hwndMain, win32con.WM_KEYUP, hotkey_value, 0)

            if len(Buff.active_buffs) == 9:
                if self.name == "heal":
                    time.sleep(random.uniform(self.cast_time * random.uniform(0.364871, 0.854326), self.cast_time * random.uniform(0.947841, 1.326363)))
                if self.name == "holy_cross":
                    time.sleep(random.uniform(self.cast_time * random.uniform(0.50834633, 0.57841235), self.cast_time * random.uniform(0.84135841, 1.057168741)))

            if self.name not in ["heal", "holy_cross"]:
                self.on_cooldown = True
                self.cooldown_started = datetime.now()
                buff_active_time = 250 + (int_value * self.int_scaling)
                self.buff_cooldown_expiration = self.cooldown_started + timedelta(seconds=buff_active_time)
                min_sleep_time = self.cast_time
                Buff.active_buffs.append(self)
                time.sleep(random.uniform(min_sleep_time, min_sleep_time + random.uniform(Buff.random_min, Buff.random_max)))

        except Exception as e:
            print(e)


    @staticmethod
    def load_skills():
        skill_data_file = os.path.join(windowproperties.WindowProperties.config_directory, Buff.skills_json_file)
        buffs = []
        with open(skill_data_file, 'r') as json_file:
            skill_data = json.load(json_file)
            for skill in skill_data['buffs']:
                buffs.append(Buff(skill))
        return buffs
    
    @staticmethod
    def clear_cooldowns(buffs):
        for buff in buffs:
            buff.on_cooldown = False
            buff.cooldown_started = ""
            buff.buff_cooldown_expiration = 0
        Buff.active_buffs = []
