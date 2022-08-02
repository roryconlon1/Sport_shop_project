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

product_1 = Product("Football", "size 5 mitre", 7, 3, 10, "Ball", sport_1)
product_repository.save(product_1)

product_2 = Product("Racket", "Wilson - Red", 5, 35, 50, "Equipment", sport_2)
product_repository.save(product_2)

product_3 = Product("Puck", "Bauer - Black", 3, 1, 4, "Equipment", sport_3)
product_repository.save(product_3)