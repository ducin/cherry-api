from urllib2 import urlopen
import urllib
import json
import unittest

from outcomes import Outcomes

MIME_HTML = 'text/html;charset=utf-8'
MIME_JSON = 'application/json'
URL = 'http://localhost:8080'

class ApplicationTest(unittest.TestCase):

    def test_index(self):
        u = urlopen(URL)
        self.assertEqual(u.getcode(), 200)
        self.assertEqual(URL, u.geturl())
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_HTML])
        content = [line for line in u][0]
        self.assertRegexpMatches(content, 'Hello world')

    def assertOutcomeIsCorrect(self, outcome):
        self.assertTrue(outcome.has_key('id'))
        self.assertTrue(type(outcome['id']) is int)
        self.assertTrue(outcome.has_key('category_id'))
        self.assertTrue(type(outcome['category_id']) is int)
        self.assertTrue(outcome.has_key('created_at'))
        self.assertTrue(type(outcome['created_at']) is unicode)
        self.assertTrue(outcome.has_key('created_by'))
        self.assertTrue(type(outcome['created_by']) is int)
        self.assertTrue(outcome.has_key('amount'))
        self.assertTrue(type(outcome['amount']) is float)
        self.assertTrue(outcome.has_key('description'))
        self.assertTrue(type(outcome['description']) is unicode)

    def test_list(self):
        u = urlopen(URL + '/outcomes')
        self.assertEqual(u.getcode(), 200)
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_JSON])
        data = json.loads([line for line in u][0])
        self.assertIsInstance(data['objects'], list)
        self.assertIsInstance(data['meta'], dict)
        for outcome in data['objects']:
            self.assertOutcomeIsCorrect(outcome)

    def test_show(self):
        u = urlopen(URL + '/outcomes/1')
        self.assertEqual(u.getcode(), 200)
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_JSON])
        content = [line for line in u][0]
        outcome = json.loads(content)
        O = Outcomes()
        self.assertEqual(outcome, O.getOneBy('1'))
        self.assertOutcomeIsCorrect(outcome)

    def test_add(self):
        params = {
            'category_id': 2,
            'amount': 2.0,
            'created_by': 2,
            'created_at': '2013-09-02 00:00:00',
            'description': 'dunno what'
        }
        params = urllib.urlencode(params)
        f = urllib.urlopen(URL + '/outcomes', params)
