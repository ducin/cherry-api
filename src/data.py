import os, ConfigParser

c = ConfigParser.ConfigParser()
c.read(os.path.abspath('./src/config/config.ini'))

sql_config = {
    'host': c.get('mysql','host'),
    'user': c.get('mysql','username'),
    'passwd': c.get('mysql','password'),
    'db': c.get('mysql','database')
}

import MySQLdb

class DatabaseHandler(object):
    def __init__(self):
        self.db = MySQLdb.connect(**sql_config)

    def select(self, fields, table):
        query = "SELECT " +', '.join(['`' + field + '`' for field in fields])
        query += "FROM " + table
        return query

    def fetch(self, query, fetcher=None):
        cur = self.db.cursor()
        cur.execute(query)
        all = cur.fetchall()
        return [fetcher(row) for row in all] if fetcher is not None else all

db_handler = DatabaseHandler()
