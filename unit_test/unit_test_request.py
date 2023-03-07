import sys
sys.path.append("..")
import json
import unittest
from unittest.mock import patch
from app import app, Inventory, ItemQO, FilterQO

class RequestTestCase(unittest.TestCase):

    @patch.object(Inventory, 'insert')
    def test_insert(self, mock_insert):
        mock_insert.return_value = {"id": 1}
        itemQo = ItemQO('item1', 'category1', 10)
        with app.test_client() as client:
            response = client.post('/insert',
                                   data=json.dumps(itemQo.__dict__),
                                   content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), {"id": 1})
        mock_insert.assert_called_once()
    
    @patch.object(Inventory, 'filter')
    def test_filter(self, mock_filter):
        ret_json =  {"items": [{
                "id": 135,
                "name": "Notebook",
                "category": "Stationary",
                "price": 5.5
                }],
            "total_price": 23.5
        }
        mock_filter.return_value = ret_json
        filterQo = FilterQO("2023-03-07 19:00:00", "2023-03-07 20:00:00")
        with app.test_client() as client:
            response = client.post('/filter',
                                   data=json.dumps(filterQo.__dict__),
                                   content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), ret_json)
        mock_filter.assert_called_once()
    
    @patch.object(Inventory, 'categorize')
    def test_category(self, mock_category):
        ret_json = {"items": [{
            "category": "Stationary",
            "total_price": 5.5,
            "count": 1
            }]
        }
        mock_category.return_value = ret_json
        with app.test_client() as client:
            response = client.post('/category',
                                   data=json.dumps({"category": "all"}),
                                   content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data), ret_json)
        mock_category.assert_called_once()

if __name__ == '__main__':
    unittest.main()