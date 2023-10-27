from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('mongodb://mongo:27017/') 

db = client['mydatabase']  
collection = db['data']  

@app.route('/api/getall', methods=['GET'])
def get_all_data():
    data = list(collection.find({}, {'_id': False})) 
    return jsonify(data)

@app.route('/api/change/<key>', methods=['PUT'])
def change_data(key):
    new_data = request.get_json()
    value = new_data.get("value")
    if value:
        collection.update_one({"key": key}, {"$set": {"value": value}})
        return jsonify({"message": f"Data with key {key} updated"})
    else:
        return jsonify({"error": "New value must be provided in the request."})

@app.route('/api/create', methods=['POST'])
def create_data():
    data = request.get_json()
    key = data.get("key")
    value = data.get("value")
    if key and value:
        inserted_id = collection.insert_one({"key": key, "value": value}).inserted_id
        return jsonify({"message": f"Data created with key: {key} and id: {inserted_id}"})
    else:
        return jsonify({"error": "Key and value must be provided in the request."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)