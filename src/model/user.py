from . import Model

class Users(Model):
    table = 'users'
    definition = [
        {'field': 'id', 'required': False, 'ptype': int, 'dbtype': 'bigint(20)'},
        {'field': 'first_name', 'required': True, 'ptype': unicode, 'dbtype': 'varchar(255)'},
        {'field': 'last_name', 'required': True, 'ptype': unicode, 'dbtype': 'varchar(255)'},
        {'field': 'email_address', 'required': True, 'ptype': unicode, 'dbtype': 'varchar(255)'},
        {'field': 'username', 'required': True, 'ptype': unicode, 'dbtype': 'varchar(128)'},
    ]
