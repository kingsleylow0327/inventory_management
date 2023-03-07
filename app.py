from flask import Flask, request
from model import db, Inventory
from query_object.itemQO import ItemQO
from query_object.filterQO import FilterQO
from config import Config

app = Flask(__name__)
config = Config()
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/insert', methods=['POST'])
def insert():
    request_data = request.get_json()
    itemQo = ItemQO(request_data.get('name', ''),
                    request_data.get('category', ''),
                    request_data.get('price', ''))
    return Inventory.insert(itemQo)

@app.route('/filter', methods=['POST'])
def filter():
    request_data = request.get_json()
    filterQo = FilterQO(request_data.get('dt_from', ''),
                    request_data.get('dt_to', ''))
    return Inventory.filter(filterQo)

@app.route('/category', methods=['POST'])
def category():
    request_data = request.get_json()
    return Inventory.categorize(request_data.get('category',''))

if __name__ == '__main__':
    app.run(debug=True)