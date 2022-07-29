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