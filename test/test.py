from urllib2 import urlopen
import unittest

MIME_HTML = 'text/html;charset=utf-8'
URL = 'http://localhost:8080'

class ExampleTest(unittest.TestCase):

    def test_app(self):
        u = urlopen(URL)
        self.assertEqual(u.getcode(), 200)
        self.assertEqual(URL, u.geturl())
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_HTML])
        content = [line for line in u]
        self.assertEqual(content, ['Hello world from CherryPy API.'])
