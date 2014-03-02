from urllib2 import urlopen, HTTPError
import urllib
import json
import unittest

HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404

MIME_HTML = 'text/html;charset=utf-8'
MIME_JSON = 'application/json'

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.config = {
            'api_url': 'http://localhost:8081'
        }

    def assertUrlIsCorrect(self, url_obj, mime):
        self.assertEqual(url_obj.getcode(), HTTP_OK)
        meta = url_obj.info()
        self.assertTrue(mime in meta.getheaders('content-type'))

    def assertUrlNotFound(self, exception, mime):
        self.assertEqual(exception.code, HTTP_NOT_FOUND)
        self.assertTrue(mime in exception.headers.get('content-type'))

#------------------------------------------------------------------------------

class BaseModelTestCase(BaseTestCase):

    def assertObjectIsCorrect(self, obj):
        for p in self.model.definition:
            field = p['field']
            ptype = p['ptype']
            self.assertTrue(obj.has_key(field), 'Field ' + field + ' should exist')
            self.assertTrue(type(obj[field]) is ptype, 'Field ' + field + ' should be of type ' + str(ptype) + ', ' + str(type(obj[field])) + ' given')

    def run_list(self):
        u = urlopen(self.config['api_url'] + '/' + self.url)
        self.assertUrlIsCorrect(u, MIME_JSON)
        response = json.loads([line for line in u][0])
        self.assertIsInstance(response['objects'], list)
        self.assertIsInstance(response['meta'], dict)
        for obj in response['objects']:
            self.assertObjectIsCorrect(obj)

    def run_show(self, obj_id, obj_compared):
        u = urlopen(self.config['api_url'] + '/' + self.url + '/' + str(obj_id))
        self.assertUrlIsCorrect(u, MIME_JSON)
        content = [line for line in u][0]
        obj = json.loads(content)
        self.assertEqual(obj, obj_compared)
        self.assertObjectIsCorrect(obj)

    def run_not_found(self, obj_id):
        try:
            u = urlopen(self.config['api_url'] + '/' + self.url + '/' + str(obj_id))
            self.fail('This should not be reached')
        except HTTPError, e:
            self.assertUrlNotFound(e, MIME_HTML)

    def run_add(self, params):
        u = urllib.urlopen(self.config['api_url'] + '/' + self.url, urllib.urlencode(params))
