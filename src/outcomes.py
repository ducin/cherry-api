import cherrypy

from data import db_handler, Model

class Outcomes(Model):
    exposed = True
    resource = 'outcomes'
    table = 'outcome'
    definition = [
        {'field': 'id', 'ptype': int, 'dbtype': 'bigint(20)'},
        {'field': 'category_id', 'ptype': int, 'dbtype': 'bigint(20)'},
        {'field': 'amount', 'ptype': float, 'dbtype': 'decimal(10,2)'},
        {'field': 'description', 'ptype': unicode, 'dbtype': 'text'},
        {'field': 'created_at', 'ptype': unicode, 'dbtype': 'datetime'},
        {'field': 'created_by', 'ptype': int, 'dbtype': 'bigint(20)'},
    ]

    def __init__(self):
        self.db = db_handler
        query = self.db.select(fields=self.fields(), table=self.table)
        # print self.db.fetch(query)
        self.objects = [
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

    @cherrypy.tools.json_out()
    def POST(self, category_id, created_at, created_by, amount, description):
        id = max([el['id'] for el in self.objects]) + 1
        self.objects.append({
            'id': id,
            'category_id': int(category_id),
            'created_at': created_at,
            'created_by': int(created_by),
            'amount': float(amount),
            'description': description
        })
        return id
