import cherrypy
from outcomes import Outcomes

class Index(object):
    def index(self):
        return "<p>Hello world from CherryPy API.</p>" + \
            "<ul>" + \
            "<li><a href=\"users\">users</a></li>" + \
            "<li><a href=\"incomes\">incomes</a></li>" + \
            "<li><a href=\"outcomes\">outcomes</a></li>" + \
            "<li><a href=\"categories\">categories</a></li>" + \
            "</ul>"
    index.exposed = True

def run():
    cherrypy.tree.mount(Index())
    cherrypy.tree.mount(
        Outcomes(), '/outcomes',
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
