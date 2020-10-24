<!-- Flaskrestapi documentation master file, created by
sphinx-quickstart on Sat Oct 24 21:09:44 2020.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Welcome to Flaskrestapi’s documentation!

## Introduction
Flaskrest API is a restful api built on Flask using python. This API can perform CRUD operations
i.e. Create, Read, Update and Delete. It is linked to a Database which is hosted on MongoDB Atlas
which consists of details of 5000 products  

```bash
Product Details as follows:  
name : Name of the product  
brand_name : brand name of the product  
regular_price_value : regular price of the product  
offer_price_value : offer price value of the product  
currency : ‘GBP’, ‘INR’ etc.  
classification_l1 : l1 class of product  
classification_l2 : l2 class of product  
classification_l3 : l3 class of product  
classification_l4 : l4 class of product  
url : url of the product  
```

## Deploy the docker container.

Run with Docker

```bash
docker run -it -d -p 5000:5000 flaskapp
```

## APIs on localhost

Run an localhost

```bash
http://localhost:5000/api/products
```

## Perform CRUD operations

Following are the commands to perform CRUD operations


## 1. List all the items

```bash
http://localhost:5000/api/products
```

## 2. Query items
```bash
http://localhost:5000/api/<arguments>/<value>
```
arguments : specification of the product  
value : value of the specification    


## 3. Add a new product
```bash
http://localhost:5000/api/<name>/<brand_name>/<regular_price_value>/<offer_price_value>/<currency>/<classification_l1>/<classification_l2>/<classification_l3>/<classification_l4>/<url>
```

name : Name of the new product
brand_name : brand name of the new product  
regular_price_value : regular price of the new product  
offer_price_value : offer price value of the new product  
currency : ‘GBP’, ‘INR’ etc  
classification_l1 : l1 class of new product  
classification_l2 : l2 class of new product  
classification_l3 : l3 class of new product  
classification_l4 : l4 class of new product  
url : url of the new product  


## 4. Delete a product

```bash
    http://localhost:5000/api/delete/<argument>/<value>
```

## 5. Update a product
```bash
    http://localhost:5000/api/update/<key>/<value>/<element>/<updateValue>
```
key : specification of the product  
value : value of the key  
element : specification of the product to update/edit  
updateValue : value to update to  
