from urllib2 import urlopen
import json
import unittest

import application
from songs import Songs

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

    def assertSongIsCorrect(self, song):
        self.assert_(song.has_key('id'))
        self.assert_(song.has_key('title'))
        self.assert_(song.has_key('artist'))

    def test_list(self):
        u = urlopen(URL + '/songs')
        self.assertEqual(u.getcode(), 200)
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_JSON])
        content = [line for line in u][0]
        data = json.loads(content)
        self.assertEqual(data, Songs.songs)
        for song in data:
            self.assertSongIsCorrect(song)

    def test_show(self):
        u = urlopen(URL + '/songs/1')
        self.assertEqual(u.getcode(), 200)
        meta = u.info()
        self.assertEqual(meta.getheaders('content-type'), [MIME_JSON])
        content = [line for line in u][0]
        song = json.loads(content)
        S = Songs()
        self.assertEqual(song, S.getOneBy('1'))
        self.assertSongIsCorrect(song)
