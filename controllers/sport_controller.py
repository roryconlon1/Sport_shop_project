from flask import Flask, render_template, request, redirect
from models.product import Product
from models.sport import Sport
from repositories import sport_repository, product_repository

from flask import Blueprint

products_blueprint = Blueprint("products", __name__)
sports_blueprint = Blueprint("sports", __name__)

@sports_blueprint.route('/sports')
def index():
    sports = sport_repository.select_all()
    return render_template('/sports/index.html', sports=sports)

@sports_blueprint.route('/sports/<id>')
def show(id):
    sport = sport_repository.select(id)
    return render_template('/sports/sport.html', sport=sport)