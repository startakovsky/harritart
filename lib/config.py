import os
import logging
import yaml


REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

def read_yaml(path):
    with open(path) as f:
        data = yaml.load(f)
    return data

def get_config_file_path(file_name, dir_path=None):
    if dir_path is None:
        config_dir = os.path.join(REPO_DIR, 'config')
    else:
        config_dir = dir_path
    return os.path.join(config_dir, file_name)

def get_config_file(file_name, dir_path=None):
    config_path = get_config_file_path(file_name, dir_path=dir_path)
    data = read_yaml(config_path)
    return data

def get_logger(calling_module):
    pass

def get_config():
    config = Config()
    config.env = os.environ['BOOST_ENV']
    config.output_dbserver = 'other'
    return config

