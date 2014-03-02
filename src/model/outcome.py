from . import Model

class Outcomes(Model):
    table = 'outcome'
    definition = [
        {'field': 'id', 'required': False, 'ptype': int, 'dbtype': 'bigint(20)'},
        {'field': 'category_id', 'required': True, 'ptype': int, 'dbtype': 'bigint(20)'},
        {'field': 'amount', 'required': True, 'ptype': float, 'dbtype': 'decimal(10,2)'},
        {'field': 'description', 'required': True, 'ptype': unicode, 'dbtype': 'text'},
        {'field': 'created_at', 'required': True, 'ptype': unicode, 'dbtype': 'datetime'},
        {'field': 'created_by', 'required': True, 'ptype': int, 'dbtype': 'bigint(20)'},
    ]
