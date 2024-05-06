"""
this is like the middleware which can help parse all the configs and gen the configs
1. read the config file
2. parse and get all dict and params from the config file
3. transfer them into a specific format that is fit
   for generate the interface for swtiching
4. generate the new config file into a path and return the path(give it to model_builder)
"""
import os

# 1. scan and get the folder or file list
def list_from_folder(folder_path='../configs', mode='d'):
    assert mode in ('d', 'a', 'f')
    if mode == 'd':
        return [f.path for f in os.scandir(folder_path) if f.is_dir()]
    elif mode == 'f':
        return [f.name for f in os.scandir(folder_path) if f.is_file()]
    elif mode == 'a':
        return [f.name for f in os.scandir(folder_path)]

# 2. (parse configs) and (generate configs from dict)
# def config_parse():
    