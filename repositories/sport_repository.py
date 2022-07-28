from db.run_sql import run_sql

from models.product import Product
from models.sport import Sport
import repositories.product_repository as product_repository
import repositories.sport_repository as sport_repository

def delete_all():
    sql = "DELETE FROM sports"
    run_sql(sql)

def save(sport):
    sql = "INSERT INTO sports (name) VALUES (%s) RETURNING id "
    values = [sport.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    sport.id = id

def select_all():
    sports = []

    sql = "SELECT * FROM sports"
    results = run_sql(sql)

    for row in results:
        sport = Sport(row['name'], row['id'])
        sports.append(sport)
    return sports

def select(id):
    sport = None
    sql = "SELECT * FROM sports where id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        sport = Sport(result['name'], result['id'])
    return sport

    