import pdb
from models.product import Product
from models.sport import Sport
import repositories.product_repository as product_repository
import repositories.sport_repository as sport_repository

product_repository.delete_all()
sport_repository.delete_all()

sport_1 = Sport("Football", True)
sport_repository.save(sport_1)

sport_2 = Sport("Tennis", False)
sport_repository.save(sport_2)

sport_3 = Sport("Ice Hockey", True)
sport_repository.save(sport_3)

product_1 = Product("Football", "Size-5, Mitre", 7, 5, 14, "Ball", sport_1)
product_repository.save(product_1)

product_2 = Product("Racket", "Wilson Blade Pro - Red", 5, 35, 100, "Equipment", sport_2)
product_repository.save(product_2)

product_3 = Product("Ice Skates", "Bauer Vapor Hyperlite - Black", 3, 500, 700, "Equipment", sport_3)
product_repository.save(product_3)

product_4 = Product("Pack of 3 Tennis Balls", "Babolat - Pro Tour", 100, 4, 10, "Ball", sport_2)
product_repository.save(product_4)

product_5 = Product("Football Boots", "Nike - Mercurial Vapors", 3, 52, 125, "Equipment", sport_1)
product_repository.save(product_5)

product_6 = Product("Helmet", "CCM Tacks 70", 10, 47, 90, "Equipment", sport_3)
product_repository.save(product_6)

product_7 = Product("Shin Pads", "G-Form Pro-s Elite", 0, 20, 45, "Equipment", sport_1)
product_repository.save(product_7)
