import windowproperties, os, json
import random, time
from datetime import datetime, timedelta
import win32con
import win32api

class Buff:

    skills_json_file = 'skills.json'
    random_min = 0.37448262
    random_max = 0.58573920
    active_buffs = []
    vk_code_json = "vk_code.json"
    spells = ["heal", "holy_cross"]

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
    def map_input_hotkey(buff):
        if not buff.has_assigned_hotkey():
            return None
        vk_code_json_path = os.path.join(windowproperties.WindowProperties.config_directory, Buff.vk_code_json)
        with open(vk_code_json_path, 'r') as json_file:
            vk_code_map = json.load(json_file)
        return int(vk_code_map.get(buff.hotkey_input), 16)
    
    @staticmethod
    def clear_cooldowns(buffs):
        for buff in buffs:
            buff.on_cooldown = False
            buff.cooldown_started = ""
            buff.buff_cooldown_expiration = 0
        Buff.active_buffs = []

    def __init__(self, skill):
        self.name = skill['name']
        self.cool_down = skill['cool_down']
        self.hotkey_input = str(skill['hotkey']).lower()
        self.mapped_key = Buff.map_input_hotkey(self)
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

        #MOVE TO DIFFERENT CLASS (character?)
        self.int_value = 213

    def is_still_active(self):
        if self.name not in Buff.spells and self.cooldown_started != "" and len(Buff.active_buffs) > 0:
            if(datetime.now() < self.buff_cooldown_expiration):
                print("[", datetime.now(), "]", self.name, "on cooldown until: [", self.buff_cooldown_expiration, "]")
                return True
            print("[", datetime.now(), "] ", self.name, "off cooldown")
            Buff.active_buffs.remove(self)     
        return False

    def has_assigned_hotkey(self):
        return self.hotkey_input not in [None, 'none', ""]

    def cast_buff(self, window_handler):
        self.print()
        win32api.SendMessage(window_handler, win32con.WM_KEYDOWN, self.mapped_key, 0)
        time.sleep(random.uniform(random.uniform(0.39572048,0.58236452), random.uniform(0.626483, 0.8448473)))
        win32api.SendMessage(window_handler, win32con.WM_KEYUP, self.mapped_key, 0)

    def reduce_cast_rate(self):
        if self.name == "heal":
            time.sleep(random.uniform(self.cast_time * random.uniform(0.364871, 0.854326), self.cast_time * random.uniform(0.947841, 1.326363)))
        if self.name == "holy_cross":
            time.sleep(random.uniform(self.cast_time * random.uniform(0.50834633, 0.57841235), self.cast_time * random.uniform(0.84135841, 1.057168741)))

    def trigger_cooldown(self):
        self.on_cooldown = True
        self.cooldown_started = datetime.now()
        buff_active_time = self.base_value + (self.int_value * self.int_scaling)
        self.buff_cooldown_expiration = self.cooldown_started + timedelta(seconds=buff_active_time)
        min_sleep_time = self.cast_time
        Buff.active_buffs.append(self)
        time.sleep(random.uniform(min_sleep_time, min_sleep_time + random.uniform(Buff.random_min, Buff.random_max)))

    def print(self):
        print("[", datetime.now(), "]", "Used", self.name)
