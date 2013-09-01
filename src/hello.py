import cherrypy

class HelloWorld(object):
    def index(self):
        return "Hello world!"
    index.exposed = True

def run():
    cherrypy.quickstart(HelloWorld())

def stop():
    cherrypy.engine.stop()

if __name__ == '__main__':
    run()
