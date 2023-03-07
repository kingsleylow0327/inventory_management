import sys
sys.path.append("..")
import unittest
from unittest.mock import patch, MagicMock
from model import Inventory
from query_object.itemQO import ItemQO

class UpdateTestCase(unittest.TestCase):

    @patch('model.Inventory.query')
    @patch('model.Inventory._is_exsisted')
    @patch('app.db.session')
    def test_update(self, mock_session, mock_is_existed, mock_inventory_instance):
        mock_session.commit = MagicMock()
        mock_session.refresh = MagicMock()
        mock_is_existed.return_value = True

        itemQo = ItemQO("test item", "test category", "10.99")

        result = Inventory.insert(itemQo)

        mock_is_existed.assert_called_once()
        mock_inventory_instance.filter_by.assert_called_once()
        mock_session.commit.assert_called_once()
        self.assertTrue("id" in result)

    
if __name__ == '__main__':
    unittest.main()