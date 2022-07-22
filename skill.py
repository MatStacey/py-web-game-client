import windowproperties, os, json
import random, time
from datetime import datetime, timedelta
import win32con
import win32api
import pyautogui

class Skill:

    skills_json_file = 'skills.json'
    random_min = 0.37448262
    random_max = 0.58573920
    active_buffs = []
    vk_code_json = "vk_code.json"
    spells = ["heal", "holy_cross"]

    @staticmethod
    def reset_buffs(buffs):
         Skill.clear_cooldowns(buffs)
         Skill.active_buffs = []

    @staticmethod
    def load_buffs():
        skill_data_file = os.path.join(windowproperties.WindowProperties.config_directory, Skill.skills_json_file)
        buffs = []
        with open(skill_data_file, 'r') as json_file:
            skill_data = json.load(json_file)
            for buff_json in skill_data['skills']['buffs']:
                buffs.append(Skill(buff_json))
        return buffs

    @staticmethod
    def load_spells():
        skill_data_file = os.path.join(windowproperties.WindowProperties.config_directory, Skill.skills_json_file)
        buffs = []
        with open(skill_data_file, 'r') as json_file:
            skill_data = json.load(json_file)
            for spell in skill_data['skills']['spells']:
                buffs.append(Skill(spell))
        return buffs


    @staticmethod
    def map_input_key(buff, key):
        if not buff.has_assigned_hotkey() or not key or key == "":
            return None
        vk_code_json_path = os.path.join(windowproperties.WindowProperties.config_directory, Skill.vk_code_json)
        with open(vk_code_json_path, 'r') as json_file:
            vk_code_map = json.load(json_file)
        return int(vk_code_map.get(key), 16)
    
    @staticmethod
    def clear_cooldowns(buffs):
        for buff in buffs:
            buff.on_cooldown = False
            buff.cooldown_started = ""
            buff.buff_cooldown_expiration = 0
        Skill.active_buffs = []

    def __init__(self, skill):
        self.name = skill['name']
        self.cool_down = skill['cool_down']
        self.hotkey_input = str(skill['hotkey']).lower().strip()
        self.modifier_input = str(skill['modifier']).lower().strip()
        self.action_bar_hotkey = str(skill['action_bar']).lower().strip()
        self.mapped_modifier = Skill.map_input_key(self, self.modifier_input)
        self.mapped_key = Skill.map_input_key(self, self.hotkey_input)
        self.action_bar = Skill.map_input_key(self, self.action_bar_hotkey)
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

    def is_active(self):
        if self.name not in Skill.spells and self.cooldown_started != "" and len(Skill.active_buffs) > 0:
            if(datetime.now() < self.buff_cooldown_expiration):
                print("[", datetime.now(), "]", self.name, "on cooldown until: [", self.buff_cooldown_expiration, "]")
                return True
            print("[", datetime.now(), "] ", self.name, "off cooldown")
            Skill.active_buffs.remove(self)     
        return False

    def has_assigned_hotkey(self):
        return self.hotkey_input.strip() not in [None, 'none', ""]

    def cast(self, window_handler):
        self.print()
        if self.modifier_input and self.modifier_input != "":
            win32api.SendMessage(window_handler, win32con.WM_KEYDOWN, self.mapped_modifier, 0)

        win32api.SendMessage(window_handler, win32con.WM_KEYDOWN, self.mapped_key, 0)
        time.sleep(random.uniform(random.uniform(0.39572048,0.58236452), random.uniform(0.626483, 0.8448473)))
        win32api.SendMessage(window_handler, win32con.WM_KEYUP, self.mapped_key, 0)

        if self.modifier_input and self.modifier_input != "":
            win32api.SendMessage(window_handler, win32con.WM_KEYUP, self.mapped_modifier, 0)


    def reduce_cast_rate(self):
        time.sleep(random.uniform(self.cast_time * random.uniform(0.50834633, 0.57841235), self.cast_time * random.uniform(0.84135841, 1.057168741)))

    def set_as_active(self):
        self.on_cooldown = True
        self.cooldown_started = datetime.now()
        buff_active_time = self.base_value + (self.int_value * self.int_scaling)
        self.buff_cooldown_expiration = self.cooldown_started + timedelta(seconds=buff_active_time)
        min_sleep_time = self.cast_time
        Skill.active_buffs.append(self)
        time.sleep(random.uniform(min_sleep_time, min_sleep_time + random.uniform(Skill.random_min, Skill.random_max)))

    def print(self):
        print("[", datetime.now(), "]", "Used", self.name)
