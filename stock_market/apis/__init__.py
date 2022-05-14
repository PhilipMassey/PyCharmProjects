from .seeking_alpha import *
from os.path import join
import configparser
config = configparser.RawConfigParser()

config_file_path = '/Users/philipmassey/.tokens/'
pycharm_path = join(config_file_path, 'pycharm.cfg')

config.read(pycharm_path)
seeking_alpha_key = config.get('rapid_api', 'seeking_alpha_key')

db_seeking_alpha_history = 'seeking_alpha_history'
#print(seeking_alpha_key)
