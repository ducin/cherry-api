from urllib2 import urlopen
import urllib
import json

from base import *
from outcomes import Outcomes

class ApplicationTest(BaseTest):

    def test_index(self):
        u = urlopen(URL)
        self.assertEqual(u.getcode(), 200)
        self.assertEqual(URL, u.geturl())
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_HTML])
        content = [line for line in u][0]
        self.assertRegexpMatches(content, 'Hello world')

    outcome_definition = {
        'id': int,
        'category_id': int,
        'created_at': unicode,
        'created_by': int,
        'amount': float,
        'description': unicode
    }

    def assertOutcomeIsCorrect(self, outcome):
        for field in self.outcome_definition:
            self.assertTrue(outcome.has_key(field))
            self.assertTrue(type(outcome[field]) is self.outcome_definition[field])

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
