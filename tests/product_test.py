import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("football", "size 5", 3, 8, 10, "Ball" ,"football")

    def test_has_name(self):
        self.assertEqual("football", self.product.name)

    def test_has_description(self):
        self.assertEqual("size 5", self.product.description)

    def test_has_stock_quantity(self):
        self.assertEqual(3, self.product.stock_quantity)

    def test_has_buying_cost(self):
        self.assertEqual(8, self.product.buying_cost)

    def test_has_selling_price(self):
        self.assertEqual(10, self.product.selling_price)

    def test_has_sport(self):
        self.assertEqual("football", self.product.sport)

    def test_has_type(self):
        self.assertEqual("Ball", self.product.product_type)