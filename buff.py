import windowproperties, os, json

class Buff:

    skills_json_file = 'skills.json'

    def __init__(self, skill):
        self.name = skill['name']
        self.cool_down = skill['cool_down'],
        self.base_value = skill['base_value'],
        self.int_scaling = skill['int_scaling'],
        self.cast_time = skill['cast_time'],
        self.level = skill['level'],
        self.max_level = skill['max_level'],
        self.scales_on = skill['scales_on'],
        self.tier = skill['tier'],
        self.job = skill['job']

    @staticmethod
    def load_skills():
        skill_data_file = os.path.join(windowproperties.WindowProperties.config_directory, Buff.skills_json_file)
        buffs = []
        with open(skill_data_file, 'r') as json_file:
            skill_data = json.load(json_file)
            for skill in skill_data['buffs']:
                buffs.append(Buff(skill))
        return buffs