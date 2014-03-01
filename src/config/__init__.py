import os, ConfigParser

config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini')
c = ConfigParser.ConfigParser()
c.read(config_file)

sql_connection = dict(c.items('mysql'))
