from flask import Flask, render_template, request, redirect
from models.product import Product
from models.sport import Sport
from repositories import sport_repository, product_repository

from flask import Blueprint

products_blueprint = Blueprint("products", __name__)
sports_blueprint = Blueprint("sports", __name__)