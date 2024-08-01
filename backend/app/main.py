from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client['advocate_app']
collection = db['contacts']

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({"message": "Agradecemos o seu contato, em breve entraremos em contato!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
