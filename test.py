import json
import pathlib
import sys, os


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'vk_code.json')
with open(file_path, 'r') as fi:
    vk_code_map = json.load(fi)

print(vk_code_map)
# with open(os.getcwd() + '\\vk_code.json', 'r') as json_file:
#     vk_code_map = json.load(json_file)

# print(vk_code_map)