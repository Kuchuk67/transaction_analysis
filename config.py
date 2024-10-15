import os
import json
PATH_HOME = os.path.dirname(os.path.abspath(__file__))



def json_setting_file() -> dict:
    '''олучить настройки для пользователя из файла'''
    file_name = 'user_settings.json'
    path_to_file = os.path.join(PATH_HOME, file_name)
    with open(path_to_file) as f:
        data = json.load(f)
    return data

JSON_SETTING = json_setting_file()
