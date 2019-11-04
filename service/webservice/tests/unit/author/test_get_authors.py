
from unittest.mock import patch, Mock
import unittest

from webservice.blueprints.api.authors.get_authors import GetAuthersApi

class TestGetAuhtor(unittest.TestCase):
    """
        Unittest for the Authors endpoints
    """

    def setUp(self) -> None:
       pass

    def tearDown(self) -> None:
       pass


    @patch.object(GetAuthersApi, "get")
    def test_get_authors_cached(self, mock_call):
        print(mock_call)
        pass


    def test_get_author_data(self):
        pass


if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetAuhtor)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    print(testResult)