from urllib.request import urlopen
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
        self.assertEqual(meta.get('content-type'), MIME_HTML)
        content = [line for line in u][0].decode("utf-8")
        self.assertEqual(content, 'Hello world from CherryPy API.')

    def assertSongIsCorrect(self, song):
        self.assert_(song.has_key('id'))
        self.assert_(song.has_key('title'))
        self.assert_(song.has_key('artist'))

    def test_list(self):
        u = urlopen(URL + '/api/songs')
        self.assertEqual(u.getcode(), 200)
        meta = u.info()
        self.assertEqual(meta.get('content-type'), MIME_JSON)
        content = [line for line in u][0].decode("utf-8")
        data = json.loads(content)
        self.assertEqual(data, server.Songs.songs)
        for song in data:
            self.assertSongIsCorrect(song)

    def test_show(self):
        u = urlopen(URL + '/api/songs/1')
        self.assertEqual(u.getcode(), 200)
        meta = u.info()
        self.assertEqual(meta.get('content-type'), MIME_JSON)
        content = [line for line in u][0].decode("utf-8")
        song = json.loads(content)
        S = server.Songs()
        self.assertEqual(song, S.getOneBy('1'))
        self.assertSongIsCorrect(song)
