from urllib2 import urlopen
import urllib
import json
import unittest

HTTP_OK = 200
HTTP_NOT_FOUND = 404

MIME_HTML = 'text/html;charset=utf-8'
MIME_JSON = 'application/json'
URL = 'http://localhost:8080'

class BaseTestCase(unittest.TestCase):

    def assertObjectIsCorrect(self, obj):
        for field in self.model.definition:
            self.assertTrue(obj.has_key(field), 'Field ' + field + ' should exist')
            self.assertTrue(type(obj[field]) is self.model.definition[field], 'Field ' + field + ' should be of type ' + str(self.model.definition[field]) + ', ' + str(type(obj[field])) + ' given')

    def assertUrlIsCorrect(self, url_obj, mime):
        self.assertEqual(url_obj.getcode(), HTTP_OK)
        meta = url_obj.info()
        self.assertTrue(mime in meta.getheaders('content-type'))

    def run_list(self):
        u = urlopen(URL + '/' + self.model.resource)
        self.assertUrlIsCorrect(u, MIME_JSON)
        response = json.loads([line for line in u][0])
        self.assertIsInstance(response['objects'], list)
        self.assertIsInstance(response['meta'], dict)
        for obj in response['objects']:
            self.assertObjectIsCorrect(obj)

    def run_show(self, obj_id, obj_compared):
        u = urlopen(URL + '/' + self.model.resource + '/' + str(obj_id))
        self.assertUrlIsCorrect(u, MIME_JSON)
        content = [line for line in u][0]
        obj = json.loads(content)
        self.assertEqual(obj, obj_compared)
        self.assertObjectIsCorrect(obj)

    # TODO: not found should return 404 HTTP CODE
    def run_not_found(self, obj_id):
        u = urlopen(URL + '/' + self.model.resource + '/' + str(obj_id))
        self.assertUrlIsCorrect(u, MIME_JSON)
        content = [line for line in u][0]
        obj = json.loads(content)
        self.assertEqual(obj, None)

    def run_add(self, params):
        u = urllib.urlopen(URL + '/' + self.model.resource, urllib.urlencode(params))
