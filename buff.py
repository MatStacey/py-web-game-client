import windowproperties, os, json
import random, time
class Buff:

    skills_json_file = 'skills.json'
    random_min = 0.37448262
    random_max = 0.58573920

    def __init__(self, skill):
        self.name = skill['name']
        self.cool_down = skill['cool_down']
        self.base_value = skill['base_value']
        self.int_scaling = skill['int_scaling']
        self.cast_time = skill['cast_time']
        self.level = skill['level']
        self.max_level = skill['max_level']
        self.scales_on = skill['scales_on']
        self.tier = skill['tier']
        self.job = skill['job']


    def get_name(self):
        return self.name

    def cast(self):
        print("Buff:", self.name, self.cool_down, self.base_value, self.int_scaling, self.cast_time, self.level, self.max_level, self.scales_on, self.tier, self.job)
        min_sleep_time = self.cast_time + self.cool_down
        time.sleep(random.uniform(min_sleep_time, min_sleep_time + random.uniform(Buff.random_min, Buff.random_max)))

    @staticmethod
    def load_skills():
        skill_data_file = os.path.join(windowproperties.WindowProperties.config_directory, Buff.skills_json_file)
        buffs = []
        with open(skill_data_file, 'r') as json_file:
            skill_data = json.load(json_file)
            for skill in skill_data['buffs']:
                buffs.append(Buff(skill))
        return buffs