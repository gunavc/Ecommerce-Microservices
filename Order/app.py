from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ecommerce"
mongo = PyMongo(app)

@app.route('/orders', methods=['POST'])
def create_order():
    orders = mongo.db.orders
    data = request.get_json()
    user_id = data.get('user_id')
    products = data.get('products')

    order = {
        'user_id': user_id,
        'products': products,
    }
    result = orders.insert_one(order)

    order['_id'] = str(order['_id'])
    print("Order Successfully Added")
    return jsonify(order), 201

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    orders = mongo.db.orders
    order = orders.find_one({'_id': order_id})
    if order:
        order['_id'] = str(order['_id'])
        return jsonify(order)
    else:
        return jsonify({'error': 'Order not found'}), 404

if __name__ == '__main__':
    app.run(port=5002, debug=True)