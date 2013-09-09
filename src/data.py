import os, ConfigParser

c = ConfigParser.ConfigParser()
c.read(os.path.abspath('./src/config/config.ini'))

sql_config = dict(c.items('mysql'))

import MySQLdb

class DatabaseHandler(object):

    def __init__(self):
        self.db = MySQLdb.connect(**sql_config)

    def select(self, fields, table, offset=None, limit=None):
        query = "SELECT " +', '.join(['`' + field + '`' for field in fields])
        query += "\nFROM " + table
        if offset is not None:
            query += "\nOFFSET " + str(offset)
        if limit is not None:
            query += "\nLIMIT " + str(limit)
        return query + ";"

    def fetch(self, query, builder=None):
        cur = self.db.cursor()
        cur.execute(query)
        all = cur.fetchall()
        return [builder(row) for row in all] if builder is not None else all

db_handler = DatabaseHandler()

import cherrypy

class Model(object):

    def getOneBy(self, value, field='id'):
        return next((el for el in self.objects if str(el[field]) == value), None)

    def fields(self):
        return [p['field'] for p in self.definition]

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
