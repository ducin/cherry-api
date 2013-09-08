import cherrypy

from data import db_handler, Model

class Users(Model):
    exposed = True
    resource = 'users'
    table = 'users'
    definition = [
        {'field': 'id', 'ptype': int, 'dbtype': 'bigint(20)'},
        {'field': 'first_name', 'ptype': unicode, 'dbtype': 'varchar(255)'},
        {'field': 'last_name', 'ptype': unicode, 'dbtype': 'varchar(255)'},
        {'field': 'email_address', 'ptype': unicode, 'dbtype': 'varchar(255)'},
        {'field': 'username', 'ptype': unicode, 'dbtype': 'varchar(128)'},
    ]
    
    def build(self, row):
        return {
            'id': row[0],
            'username': row[4],
            'first_name': row[1],
            'last_name': row[2],
            'email_address': row[3]
        }

    def __init__(self):
        self.db = db_handler
        query = self.db.select(fields=self.fields(), table=self.table)
        self.objects = self.db.fetch(query, self.build)

    @cherrypy.tools.json_out()
    def POST(self, first_name, last_name, username, email_address):
        id = max([el['id'] for el in self.objects]) + 1
        self.objects.append({
            'id': id,
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email_address': email_address
        })
        return id
