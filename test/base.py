from urllib2 import urlopen
import json
import unittest

MIME_HTML = 'text/html;charset=utf-8'
MIME_JSON = 'application/json'
URL = 'http://localhost:8080'

class BaseTestCase(unittest.TestCase):

    def assertObjectIsCorrect(self, obj):
        for field in self.obj_def:
            self.assertTrue(obj.has_key(field))
            self.assertTrue(type(obj[field]) is self.obj_def[field])

    def run_list(self, suffix):
        u = urlopen(URL + suffix)
        self.assertEqual(u.getcode(), 200)
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_JSON])
        data = json.loads([line for line in u][0])
        self.assertIsInstance(data['objects'], list)
        self.assertIsInstance(data['meta'], dict)
        for obj in data['objects']:
            self.assertObjectIsCorrect(obj)