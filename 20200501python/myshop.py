from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

products = {
  "sku01": { 
    "id": "sku01", 
    "name": "Pen", 
    "price": 15, 
    "desc": "This is a pen.",
    "image": "https://cdn11.bigcommerce.com/s-b17f1zdab8/images/stencil/1280x1280/products/257/678/117808_AT0112-18_Calais_Matte_Metallic_Blue_BP_01__94974.1541480028.jpg?c=2&imbypass=on",
  },
  "sku02": { 
    "id": "sku02", 
    "name": "Cup", 
    "price": 80, 
    "desc": "This is a cup.",
    "image": "https://cdn11.bigcommerce.com/s-555dc/images/stencil/1280x1280/products/1164/3017/18512-BL_12ozcup__94183.1549595415.jpg?c=2&imbypass=on&imbypass=on"
  },
  "sku03": { 
    "id": "sku03", 
    "name": "Notebook", 
    "price": 25, 
    "desc": "great notebook",
    "image": "https://cdn.shopify.com/s/files/1/0831/9463/products/Notebooks_Notebook_Hunter_800x.png?v=1571438791"
  },
  "sku04": { 
    "id": "sku04", 
    "name": "Stapler", 
    "price": 20, 
    "desc": "useful stapler",
    "image": "https://images-na.ssl-images-amazon.com/images/I/61GZIr9bcxL._AC_SX466_.jpg"
  },
}

mycart = {}

@app.route("/")
def myshop():
  return render_template("myshop.html", products=products)

@app.route("/product/<id>")
def product(id):
  pd = products[id]
  return render_template("product.html", product=pd)

@app.route("/cart")
def cart():
  total = 0
  for id, num in mycart.items():
    pd = products[id]
    total += pd['price'] * num

  return render_template("cart.html", mycart=mycart, products=products, total=total)

@app.route("/add-cart/<id>")
def addCart(id):
  mycart[id] = mycart.get(id, 0) + 1
  return redirect('/cart')

@app.route("/remove-cart/<id>")
def removeCart(id):
  del mycart[id]
  return redirect('/cart')

@app.route('/add-product', methods = ['GET', 'POST'])
def addProduct():
  if request.method == 'POST':
    name = request.form.get('name')
    price = request.form.get('price')
    products['sku' + str(len(products))] = { 
      'name': name, 
      'price': price
    }
    return redirect('/')

  return render_template('add-product.html')