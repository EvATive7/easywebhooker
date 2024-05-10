from webhooker import *
import yaml

import logging
logging.basicConfig(level=logging.DEBUG)

config = yaml.safe_load(open('config.yaml').read())

content = 'ok'
configure(config['webhook'])
webhook(now='finished', content=content)
webhook(now='start', content=content)
