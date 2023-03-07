import unittest
from unittest.mock import patch
import sys
sys.path.append("..")
from model import Inventory  # noqa: E402
from query_object.filterQO import FilterQO  # noqa: E402


class FilterTestCase(unittest.TestCase):

    @patch('model.Inventory')
    def test_update(self, mock_inventory_instance):
        filterQO = FilterQO("2023-03-07 19:00:00", "2023-03-07 20:00:00")
        result = Inventory.filter(filterQO)
        mock_inventory_instance.query.filter.assert_called_once()
        self.assertTrue("item" in result)
        self.assertTrue("total_price" in result)


if __name__ == '__main__':
    unittest.main()
