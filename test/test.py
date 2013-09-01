from urllib2 import urlopen
import json
import unittest
import server

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
        content = [line for line in u]
        self.assertEqual(content[0], 'Hello world from CherryPy API.')

    def test_list(self):
        u = urlopen(URL + '/api/songs')
        self.assertEqual(u.getcode(), 200)
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_JSON])
        content = [line for line in u]
        data = json.loads(content[0])
        self.assertEqual(data, server.Songs.songs)
