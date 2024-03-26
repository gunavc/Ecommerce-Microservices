from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ecommerce"
mongo = PyMongo(app)

@app.route('/products', methods=['POST'])
def create_product():
    products = mongo.db.products
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')

    product = {
        'name': name,
        'price': price,
    }
    _ = products.insert_one(product)

    product['_id'] = str(product['_id'])
    return jsonify(product), 201

@app.route('/products', methods=['GET'])
def get_products():
    products = mongo.db.products
    product_list = [{'_id': str(product['_id']), 'name': product['name'], 'price': product['price']} for product in products.find()]
    return jsonify(product_list)

if __name__ == '__main__':
    
    app.run(port=5001, debug=True)