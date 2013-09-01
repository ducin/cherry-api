import cherrypy

class HelloWorld(object):
    def index(self):
        return "Hello world!"
    index.exposed = True

def run():
    cherrypy.quickstart(HelloWorld())

if __name__ == '__main__':
    run()
