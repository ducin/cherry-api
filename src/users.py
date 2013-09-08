import cherrypy

from data import db_handler, Model

# TODO: definition can't be represented this way. Select query builder dict .keys() which
# returns keys in undetermined order, whereas build function needs determined order
class Users(Model):
    exposed = True
    resource = 'users'
    table = 'users'
    definition = {
        'id': int,
        'first_name': unicode,
        'last_name': unicode,
        'email_address': unicode,
        'username': unicode
    }
    def build(self, row):
        return {
            'id': row[4],
            'username': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'email_address': row[3]
        }

    def __init__(self):
        self.db = db_handler
        query = db_handler.select(fields=self.definition.keys(), table=self.table)
        self.objects = self.db.fetch(query, self.build)

    @cherrypy.tools.json_out()
    def GET(self, id=None):
        if id == None:
            return {
                'meta': {
                    'limit': None,
                    'next': None,
                    'offset': None,
                    'previous': None,
                    'total_count': len(self.objects)
                },
                'objects' : self.objects
            }
        else:
            return self.getOneBy(id)

#    @cherrypy.tools.json_out()
#    def POST(self, category_id, created_at, created_by, amount, description):
#        id = max([el['id'] for el in self.objects]) + 1
#        self.objects.append({
#            'id': id,
#            'category_id': int(category_id),
#            'created_at': created_at,
#            'created_by': int(created_by),
#            'amount': float(amount),
#            'description': description
#        })
#        return id
