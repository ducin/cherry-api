from base import *
from config import connection
from model.user import Users

class UsersTest(BaseModelTestCase):
    model = Users(connection)
    url = 'users'

    def test_list(self):
        self.run_list()

    def test_show(self):
        self.run_show(1, self.model.get_one_by('1'))

    def test_not_found(self):
        self.run_not_found(0)

    def test_add(self):
        self.run_add({
            'first_name': 'Elvis',
            'last_name': 'Presley',
            'username': 'ep',
            'email_address': 'elvis.presley@rocknroll.com'
        })
