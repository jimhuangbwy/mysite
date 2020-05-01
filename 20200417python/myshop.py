from flask import Flask, render_template
from flask import request, redirect

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

cart = {
  "sku01": 2,
  "sku02": 5
}

app = Flask(__name__)

@app.route("/")
def myshop():
    total = 0
    for key in cart:
      qty = cart[key]
      item = products[key]
      total += item['price'] * qty

    return render_template("myshop.html", products=products, 
      cart=cart, total=total)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)

@app.route('/product/<id>/edit', methods = ['GET', 'POST'])
def edit(id):
    prod = products[id]
    if request.method == 'POST':
        prod['name'] = request.form['name']
        prod['price'] = int(request.form['price'])
        prod['desc'] = request.form['desc']
        prod['image'] = request.form['image']
        return redirect('/product/' + id)
    return render_template('product-edit.html', product=prod)

@app.route("/cart/edit", methods = ['GET', 'POST'])
def cartEdit():
    errors = {}
    if request.method == 'POST':
      pen = int(request.form['pen'])
      cup = int(request.form['cup'])
      if pen <= 0:
        errors['sku01'] = 'should be positive'
      if cup <= 0:
        errors['sku02'] = 'should be positive'

      if len(errors):
        return render_template("cart-edit.html", cart=cart, errors=errors)

      cart['sku01'] = pen
      cart['sku02'] = cup
      return redirect('/')

    return render_template("cart-edit.html", cart=cart, errors=errors)