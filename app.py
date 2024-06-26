from flask import Flask, request
from api.index import search, search_internet
app = Flask(__name__)

app.route('/search')(search)
app.route('/search_internet', methods=['POST'])(search_internet)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

