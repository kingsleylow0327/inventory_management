import unittest
from unittest.mock import patch, MagicMock
import sys
sys.path.append("..")
from model import Inventory  # noqa: E402
from query_object.itemQO import ItemQO  # noqa: E402


class InsertTestCase(unittest.TestCase):

    def test_to_json_exclude(self):
        item = Inventory(id="1",
                         name="Pen",
                         category="Stationary",
                         price=1.99,
                         last_updated_dt="2023-03-08")
        expected_json = {
            'name': 'Pen',
            'category': 'Stationary',
            'price': '1.99'
        }
        exclude_list = ['id', 'last_updated_dt']
        result = item.to_json_exclude(exclude_list)
        self.assertEqual(result, expected_json)

    @patch('model.Inventory._is_exsisted')
    @patch('app.db.session')
    def test_insert(self, mock_session, mock_is_existed):
        mock_session.commit = MagicMock()
        mock_session.refresh = MagicMock()
        mock_is_existed.return_value = False

        itemQo = ItemQO("test item", "test category", "10.99")

        result = Inventory.insert(itemQo)

        mock_is_existed.assert_called_once()
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        self.assertTrue("id" in result)


if __name__ == '__main__':
    unittest.main()
