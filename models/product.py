class Product:
    def __init__(self, name, description, stock_quantity, buying_cost, selling_price, sport,  id = None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.sport = sport
        self.id = id

    def markup(self):
        new_price = self.selling_price - self.buying_cost
        return new_price
