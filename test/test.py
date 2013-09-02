from urllib2 import urlopen
import json
import unittest

import application
from outcomes import Outcomes

MIME_HTML = 'text/html;charset=utf-8'
MIME_JSON = 'application/json'
URL = 'http://localhost:8080'

class ExampleTest(unittest.TestCase):

    def test_index(self):
        u = urlopen(URL)
        self.assertEqual(u.getcode(), 200)
        self.assertEqual(URL, u.geturl())
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_HTML])
        content = [line for line in u][0]
        self.assertEqual(content, 'Hello world from CherryPy API.')

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
        content = [line for line in u][0]
        data = json.loads(content)
        self.assertEqual(data, application.Outcomes.outcomes)
        for outcome in data:
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
