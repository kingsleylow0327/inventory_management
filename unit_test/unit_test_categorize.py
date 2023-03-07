import sys
sys.path.append("..")
import unittest
from unittest.mock import patch
from model import Inventory

class CategorizeTestCase(unittest.TestCase):

    @patch('app.db.session')
    def test_update(self, mock_session):
        result = Inventory.categorize("Pen")
        mock_session.query.assert_called_once()
        self.assertTrue("items" in result)
    
if __name__ == '__main__':
    unittest.main()