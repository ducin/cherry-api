import cherrypy

class Resource(object):
    exposed = True

    def __init__(self, model):
        self.model = model

    @cherrypy.tools.json_out()
    def GET(self, _id=None):
        if _id == None:
            return {
                'meta': {
                    'limit': None,
                    'next': None,
                    'offset': None,
                    'previous': None,
                    'total_count': len(self.model.fetch_all())
                },
                'objects' : self.model.fetch_all()
            }
        else:
            obj = self.model.get_one_by(_id)
            if obj:
                return obj
            else:
                raise cherrypy.HTTPError(404)

    @cherrypy.tools.json_out()
    def POST(self, **kwargs):
        if not self.model.insert(**kwargs):
            raise cherrypy.HTTPError(400)
