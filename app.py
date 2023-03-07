from flask import Flask, request
from model import db, Inventory
from itemQO import ItemQO
from config import Config

app = Flask(__name__)
config = Config()
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/insert', methods=['POST'])
def insert():
    return

@app.route('/filter', methods=['POST'])
def filter():
    return

@app.route('/category', methods=['POST'])
def category():
    return

if __name__ == '__main__':
    app.run(debug=True)