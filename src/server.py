import cherrypy

class Index(object):
    def index(self):
        return "Hello world from CherryPy API."
    index.exposed = True

def run():
    cherrypy.tree.mount(Index())
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()

def stop():
    cherrypy.engine.stop()

if __name__ == '__main__':
    run()
