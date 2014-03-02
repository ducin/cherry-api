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

    def fetch_all(self):
        return [
            {
                'id': 1,
                'category_id': 5,
                'created_at': "2011-09-01 00:00:00",
                'created_by': 2,
                'amount': 121.46,
                'description': 'mattress'
            },
            {
                'id': 2,
                'category_id': 5,
                'created_at': "2011-09-02 00:00:00",
                'created_by': 1,
                'amount': 493.68,
                'description': 'foreign currency'
            },
            {
                'id': 3,
                'category_id': 20,
                'created_at': "2013-07-21 00:00:00",
                'created_by': 2,
                'amount': 9.0,
                'description': 'holiday souvenir'
            }
        ]
