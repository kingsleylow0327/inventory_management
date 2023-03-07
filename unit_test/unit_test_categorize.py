import unittest
from unittest.mock import patch
import sys
sys.path.append("..")
from model import Inventory  # noqa: E402


class CategorizeTestCase(unittest.TestCase):

    @patch('app.db.session')
    def test_update(self, mock_session):
        result = Inventory.categorize("Pen")
        mock_session.query.assert_called_once()
        self.assertTrue("items" in result)


if __name__ == '__main__':
    unittest.main()
