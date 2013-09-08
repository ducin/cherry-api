from urllib2 import urlopen
import urllib
import json

from base import *
from outcomes import Outcomes

class OutcomeTest(BaseTestCase):

    url_suffix = '/outcomes'

    obj_def = {
        'id': int,
        'category_id': int,
        'created_at': unicode,
        'created_by': int,
        'amount': float,
        'description': unicode
    }

    def test_list(self):
        self.run_list(self.url_suffix)

    def test_show(self):
        u = urlopen(URL + self.url_suffix + '/1')
        self.assertEqual(u.getcode(), 200)
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_JSON])
        content = [line for line in u][0]
        outcome = json.loads(content)
        O = Outcomes()
        self.assertEqual(outcome, O.getOneBy('1'))
        self.assertObjectIsCorrect(outcome)

    def test_add(self):
        params = {
            'category_id': 2,
            'amount': 2.0,
            'created_by': 2,
            'created_at': '2013-09-02 00:00:00',
            'description': 'dunno what'
        }
        params = urllib.urlencode(params)
        f = urllib.urlopen(URL + self.url_suffix, params)
