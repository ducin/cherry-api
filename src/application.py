import cherrypy
from users import Users
from outcomes import Outcomes

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

def run():
    cherrypy.tree.mount(Index())
    for model in [Users(), Outcomes()]:
        cherrypy.tree.mount(
            model, '/' + model.resource,
            {'/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
            }
        )
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()

def stop():
    cherrypy.engine.stop()

if __name__ == '__main__':
    run()
