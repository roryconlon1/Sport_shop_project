from flask import Flask, render_template, request, redirect
from models.product import Product
from models.sport import Sport
from repositories import sport_repository, product_repository

from flask import Blueprint

products_blueprint = Blueprint("products", __name__)
sports_blueprint = Blueprint("sports", __name__)

@products_blueprint.route('/products')
def index():
    products = product_repository.select_all()
    return render_template('/products/index.html', products=products)

@products_blueprint.route('/products/<id>')
def show(id):
    product = product_repository.select(id)
    return render_template('/products/product.html', product=product)

@products_blueprint.route('/products/new')
def new():
    products = product_repository.select_all()
    sports = sport_repository.select_all()
    return render_template('/products/new.html', sports=sports, products=products)

@products_blueprint.route('/products', methods = ['POST'])
def create():
    name = request.form['name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    sport_id = request.form['sport_id']
    product_type = request.form['product_type']
    sport = sport_repository.select(sport_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, product_type, sport)
    product_repository.save(product)
    return redirect('/products')

@products_blueprint.route('/products/<id>/edit')
def edit(id):
    product = product_repository.select(id)
    sports = sport_repository.select_all()
    products = product_repository.select_all()
    return render_template('/products/edit.html', product=product, all_sports=sports, products=products)

@products_blueprint.route('/products/<id>', methods=['POST'])
def update(id):
    name = request.form['name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    product_type = request.form['product_type']
    sport_id = request.form['sport_id']
    sport = sport_repository.select(sport_id)
    product = Product(name, description,stock_quantity, buying_cost, selling_price, product_type, sport, id)
    product_repository.update(product)
    return redirect('/products/' + id)

@products_blueprint.route('/products/Equipment')
def equipment():
    types = product_repository.select_all()
    return render_template('/products/Equipment.html', types=types)

@products_blueprint.route('/products/Ball')
def ball():
    types = product_repository.select_all()
    return render_template('/products/Ball.html', types=types)

@products_blueprint.route('/products/Clothes')
def clothes():
    types = product_repository.select_all()
    return render_template('/products/Clothes.html', types=types)