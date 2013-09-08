from urllib2 import urlopen

from base import *

class HomepageTest(BaseTestCase):

    def test_index(self):
        u = urlopen(URL)
        self.assertEqual(u.getcode(), 200)
        self.assertEqual(URL, u.geturl())
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_HTML])
        content = [line for line in u][0]
        self.assertRegexpMatches(content, 'Hello world')
