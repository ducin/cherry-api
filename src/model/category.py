from . import Model

class Categories(Model):
    table = 'category'
    definition = [
        {'field': 'id', 'required': False, 'ptype': int, 'dbtype': 'bigint(20)'},
        {'field': 'parent_id', 'required': True, 'ptype': int, 'dbtype': 'bigint(20)'},
        {'field': 'name', 'required': True, 'ptype': unicode, 'dbtype': 'varchar(32)'},
        {'field': 'type', 'required': True, 'ptype': unicode, 'dbtype': 'enum(income,outcome)'},
        {'field': 'created_at', 'required': True, 'ptype': unicode, 'dbtype': 'datetime'},
        {'field': 'updated_at', 'required': True, 'ptype': unicode, 'dbtype': 'datetime'},
        {'field': 'created_by', 'required': True, 'ptype': int, 'dbtype': 'bigint(20)'},
        {'field': 'updated_by', 'required': True, 'ptype': int, 'dbtype': 'bigint(20)'},
    ]
