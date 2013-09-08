import cherrypy

class Outcomes:
    exposed = True
    outcomes = [
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

    def getOneBy(self, value, field='id'):
        return next((el for el in self.outcomes if str(el[field]) == value), None)

    @cherrypy.tools.json_out()
    def GET(self, id=None):
        if id == None:
            return {
                'meta': {
                    'limit': None,
                    'next': None,
                    'offset': None,
                    'previous': None,
                    'total_count': len(self.outcomes)
                },
                'objects' : self.outcomes
            }
        else:
            return self.getOneBy(id)

    @cherrypy.tools.json_out()
    def POST(self, category_id, created_at, created_by, amount, description):
        id = max([el['id'] for el in self.outcomes]) + 1
        self.outcomes.append({
            'id': id,
            'category_id': int(category_id),
            'created_at': created_at,
            'created_by': int(created_by),
            'amount': float(amount),
            'description': description
        })
        return id
