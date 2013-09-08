import cherrypy
from outcomes import Outcomes

class Index(object):
    def index(self):
        options = [
            {'label': 'users', 'href': 'users'},
            {'label': 'incomes', 'href': 'incomes'},
            {'label': 'outcomes', 'href': 'outcomes'},
            {'label': 'categories', 'href': 'categories'}
            ]
        html = "<p>Hello world from CherryPy API.</p><ul>"
        for el in options:
            html += "<li><a href='" + el['href'] + "'>" + el['label'] + "</a></li>"
        html += "</ul>"
        return html
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
