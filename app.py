from flask import Flask, request

app = Flask(__name__)

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