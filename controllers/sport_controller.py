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

@sports_blueprint.route('/sports/new')
def new():
    return render_template('/sports/new.html')

@sports_blueprint.route('/sports', methods = ['POST'])
def create():
    name = request.form['name']
    active = request.form['active']
    sport = Sport(name, active)
    sport_repository.save(sport)
    return redirect('/sports')

@sports_blueprint.route('/sports/<id>/edit')
def edit(id):
    sport = sport_repository.select(id)
    return render_template('/sports/edit.html', all_sports=sport)

@sports_blueprint.route('/sports/<id>', methods = ['POST'])
def updated(id):
    name = request.form['name']
    active = ['active']
    sport= Sport(name, active, id)
    sport_repository.update(sport)
    return redirect('/sports/' + id)

@sports_blueprint.route('/sports/<id>/bysport')
def all(id):
    sport = sport_repository.select(id)
    products = product_repository.select_all()
    return render_template('/sports/bysport.html', sport=sport, products=products)