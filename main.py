from flask import Flask, make_response, jsonify # Importing libraries
from pymongo import MongoClient

app = Flask(__name__)

# Created Cluster from Mongodb Atlas as connected using the MongoClient from pymongo library
#Hidden the password and cluster name
cluster = MongoClient("mongodb+srv://summer69:####@cluster0.uho9y.mongodb.net/###?retryWrites=true&w=majority")

db = cluster.get_database('Cluster_name')  #connecting to database in the cluster
collection = db.table #extracting the table to connect with from the database

# Code to Upload data to the Mongodb cloud server
# with open(r'C:\Users\Home\PycharmProjects\pythonProject\Greendeck SE Assignment Task 1.json') as file:
#      file_data = json.load(file)
#
# collection.insert_many(file_data)

# Creating route to extract all the products
@app.route('/api/products', methods=['GET'])
def api_products():
    all_prods = collection.find()
    output = {}
    i = 0
    for x in all_prods:
        output[i] = x
        output[i].pop('_id')
        i += 1
    return jsonify(output)
    pass

#Create route to extract products using the argument and value which matches in the table
@app.route('/api/<argument>/<value>', methods=['GET'])
def get_product(argument, value):
    """
    param argument: Taking any argument to be checked
    param value: Taking the value of the argument to be checked
    return: Returning the product which matche sthe argument and product detail
    """
    queryObj = {argument: value}
    query = collection.find(queryObj)
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i += 1
    return jsonify(output)
    pass

@app.errorhandler(400)
def not_found():
    """
    return: Returning error:not found whenever we face a 400 error
    """

    return make_response(jsonify({'error': 'Not found'}), 404)

#Create route to add a new product in the table
@app.route(
    '/api/new/<name>/<brand_name>/<regular_price_value>/<offer_price_value>/<currency>/<classification_l1'
    '>/<classification_l2>/<classification_l3>/<classification_l4>/<url>',
    methods=['POST'])
def new_product(name, brand_name, regular_price_value, offer_price_value, currency, classification_l1,
                classification_l2, classification_l3, classification_l4, url):
    queryObj = {
        'name': name,
        'brand_name': brand_name,
        'regular_price_value': regular_price_value,
        'offer_price_value': offer_price_value,
        'currency': currency,
        'classification_l1': classification_l1,
        'classification_l2': classification_l2,
        'classification_l3': classification_l3,
        'classification_l4': classification_l4,
        'image_url': url
    }

    collection.insert_one(queryObj)
    return "Query Inserted.." # Output if new entry updated in the table

#Create route to edit/ update the exisiting elements of the table
@app.route('/api/update/<key>/<value>/<element>/<updateValue>', methods=['PUT'])
def update(key, value, element, updateValue):
    queryObject = {key: value}
    updateObject = {element: updateValue}
    query = collection.update_one(queryObject, {'$set': updateObject})
    if query.acknowledged:
        return "Update Successful" # Output if the entry is updated
    else:
        return "Update Unsuccessful" # Output if the entry is not updated

#Create route to delete a entry in the table which matches the argument and value
@app.route('/api/delete/<argument>/<value>', methods=['DELETE'])
def delete_task(argument, value):
    queryObj = {argument: value}
    query = collection.delete_one(queryObj)
    if query.acknowledged:
        return "Delete Successful" # Output if the entry is deleted
    else:
        return "Delete Unsuccessful" # Output if the entry is not deleted


if __name__ == '__main__':
    app.run(debug = False)
