from db.run_sql import run_sql

from models.product import Product
from models.sport import Sport
from repositories import sport_repository

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def save(product):
    sql = "INSERT INTO products(name, description, stock_quantity, buying_cost, selling_price, product_type, sport_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.product_type, product.sport.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for product in results:
        sport = sport_repository.select(product['sport_id'])
        product = Product(product['name'], product['description'], product['stock_quantity'], product['buying_cost'], product['selling_price'], product['product_type'], sport, product['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        sport = sport_repository.select(result['sport_id'])
        product = Product(result['name'], result['description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], result['product_type'], sport, result['id'])
    return product

def update(product):
    sql = "UPDATE products SET (name, description, stock_quantity, buying_cost, selling_price, product_type, sport_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.product_type, product.sport.id, product.id]
    run_sql(sql, values)

