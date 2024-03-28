from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Ecommerce"
mongo = PyMongo(app)

#Register User
@app.route('/users', methods=['POST'])
def register_user():
    users = mongo.db.users
    data = request.get_json()
    #empid = data.get("empid")
    username = data.get('username')
    password = data.get('password')
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    min_id = 0
    res = users.find().sort({"empid":-1}).limit(1)
    for doc in res:
        min_id = doc["empid"]

    user = {
        'empid': int(min_id)+1,
        'username': username,
        'password': hashed_password.decode('utf-8'),
    }
    result = users.insert_one(user)

    user['_id'] = str(user['_id'])
    print("User Successfully Added")
    return jsonify(user), 201

#Get User
@app.route('/users/<emp_id>', methods=['GET'])
def get_user(emp_id):
    users = mongo.db.users
    user = users.find_one({'empid': emp_id}, {"_id":0})
    if user:
        user['empid'] = str(user['empid'])
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(port=5003, debug=True)