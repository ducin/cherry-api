from base import *
from users import Users

class UsersTest(BaseTestCase):
    model = Users()
    url_suffix = model.resource
    definition = model.definition

    def test_list(self):
        self.run_list()

#    def test_show(self):
#        self.run_show(1, self.model.getOneBy('1'))

    def test_not_found(self):
        self.run_not_found(0)

#    def test_add(self):
#        self.run_add({
#            'category_id': 2,
#            'amount': 2.0,
#            'created_by': 2,
#            'created_at': '2013-09-02 00:00:00',
#            'description': 'dunno what'
#        })
