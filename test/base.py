import unittest

MIME_HTML = 'text/html;charset=utf-8'
MIME_JSON = 'application/json'
URL = 'http://localhost:8080'

class BaseTest(unittest.TestCase):

    def assertObjectIsCorrect(self, obj):
        for field in self.obj_def:
            self.assertTrue(obj.has_key(field))
            self.assertTrue(type(obj[field]) is self.obj_def[field])
