import cherrypy

from config import connection, service
from resource import Resource
from model.user import Users
from model.category import Categories
from model.outcome import Outcomes

class Index(object):
    def index(self):
        options = [
            {'label': 'users', 'href': 'users'},
            {'label': 'incomes', 'href': 'incomes'},
            {'label': 'outcomes', 'href': 'outcomes'},
            {'label': 'categories', 'href': 'categories'}
            ]
        return "<p>Hello world from CherryPy API.</p>" + \
            "<ul>" + ''.join(["<li><a href='" + el['href'] + "'>" + el['label'] + "</a></li>" for el in options]) + "</ul>"
    index.exposed = True

resources = [
    (Resource(Users(connection)), '/users'),
    (Resource(Categories(connection)), '/categories'),
    (Resource(Outcomes(connection)), '/outcomes')
]

def run():
    cherrypy.tree.mount(Index())
    for resource, url_root in resources:
        cherrypy.tree.mount(
            resource, url_root,
            {'/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
        )
    cherrypy.server.socket_host = service['host']
    cherrypy.server.socket_port = int(service['port'])
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()

def stop():
    cherrypy.engine.stop()

if __name__ == '__main__':
    run()
