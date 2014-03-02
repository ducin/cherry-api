import MySQLdb
import cherrypy

class DatabaseHandler(object):

    def __init__(self, sql_conn):
        self.db = MySQLdb.connect(**sql_conn)

    def select(self, table, fields, offset=None, limit=None):
        clause_field_list = ', '.join(['`' + field + '`' for field in fields])
        query = "SELECT %s FROM %s" % (clause_field_list, table)
        if offset is not None:
            query += "\nOFFSET " + str(offset)
        if limit is not None:
            query += "\nLIMIT " + str(limit)
        return query + ";"

    def insert(self, table, fields, objects):
        values = []
        for obj in objects:
            values.append( '(' + ', '.join('\'' + obj[field] + '\'' for field in fields) + ')' )
        query = "INSERT INTO %s (%s) VALUES %s;" % (table, ', '.join(fields), ', '.join(values))
        return query

    def fetch(self, query, builder=None):
        cur = self.db.cursor()
        cur.execute(query)
        _all = cur.fetchall()
        return [builder(row) for row in _all] if builder is not None else _all

    def save(self, query):
        cur = self.db.cursor()
        try:
            cur.execute(query)
            self.db.commit()
        except:
            self.db.rollback()

class Model(object):

    def __init__(self, connection):
        self.db = DatabaseHandler(connection)

    def fetch_all(self):
        query = self.db.select(table=self.table, fields=self.fields())
        return self.db.fetch(query, self.build)

    def required_fields(self):
        return [p['field'] for p in self.definition if p['required']]

    def fields(self):
        return [p['field'] for p in self.definition]

    def get_one_by(self, value, field='id'):
        return next((el for el in self.fetch_all() if str(el[field]) == value), None)

    def insert(self, **kwargs):
        if all(field in kwargs for field in self.required_fields()):
            query = self.db.insert(table=self.table, fields=self.required_fields(), objects=[kwargs])
            return self.db.save(query)
        else:
            return False
