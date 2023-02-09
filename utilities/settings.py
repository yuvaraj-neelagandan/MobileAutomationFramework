import os
import yaml
from utilities.baseUtility import BaseUtility

if os.path.exists(BaseUtility().ROOT_PATH + "/yml/config.yml"):
    env = os.environ.get('env', 'production')
    env = env.lower()
    if env in ['production']:
        CONFIG = yaml.safe_load(open(BaseUtility().ROOT_PATH + "/yml/config.yml", 'r'))[env]
        TEST_DATA = yaml.safe_load(open(BaseUtility().ROOT_PATH + "/yml/{}.yml".format(env)))
    else:
        raise "Invalid Environment"
else:
    raise "config.yml does not exists"

platform = (CONFIG['platform'])
