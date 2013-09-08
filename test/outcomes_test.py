from base import *
from outcomes import Outcomes

class OutcomesTest(BaseTestCase):
    URL_SUFFIX = '/outcomes'
    OBJ_DEF = {
        'id': int,
        'category_id': int,
        'created_at': unicode,
        'created_by': int,
        'amount': float,
        'description': unicode
    }

    def test_list(self):
        self.run_list()

    def test_show(self):
        self.run_show(1, Outcomes().getOneBy('1'))

    def test_not_found(self):
        self.run_not_found(0)

    def test_add(self):
        self.run_add({
            'category_id': 2,
            'amount': 2.0,
            'created_by': 2,
            'created_at': '2013-09-02 00:00:00',
            'description': 'dunno what'
        })
