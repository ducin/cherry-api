import cherrypy

class Songs:
    exposed = True
    songs = [
        {
            'id': '1',
            'title': 'Lumberjack Song',
            'artist': 'Canadian Guard Choir'
        },
        {
            'id': '2',
            'title': 'Always Look On the Bright Side of Life',
            'artist': 'Eric Idle'
        },
        {
            'id': '3',
            'title': 'Spam Spam Spam',
            'artist': 'Monty Python'
        }
    ]
    def getOneBy(self, value, field='id'):
        return next((el for el in self.songs if el[field] == value), None)
    @cherrypy.tools.json_out()
    def GET(self, id=None):
        if id == None:
            return self.songs
        else:
            return self.getOneBy(id)
