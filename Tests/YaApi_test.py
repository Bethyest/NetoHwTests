import unittest
from YaApi import YDConnector

class TestYaApi(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestYaApi, self).__init__(*args, **kwargs)
        # self.ydc = None
        self.token = 'Enter your token'

    def setUp(self):
        ydc = YDConnector(self.token)

    def tearDown(self):
        del self.ydc

    def test_create_folder(self):
        self.ydc = YDConnector(self.token)
        self.assertEqual(self.ydc.create_folder('papka').status_code, 201)

    def test_delete(self):
        self.ydc = YDConnector(self.token)
        self.ydc2 = YDConnector(self.token)
        self.assertEqual(self.ydc.delete('papka').status_code, 204)
        self.assertEqual(self.ydc2.delete('papochka').status_code, 204)  # Ошибка

