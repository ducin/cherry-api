from urllib2 import urlopen

from base import *

class HomepageTest(BaseTestCase):

    def test_index(self):
        u = urlopen(self.config['api_url'])
        self.assertUrlIsCorrect(u, MIME_HTML)
        content = [line for line in u][0]
        self.assertRegexpMatches(content, 'Hello world')
