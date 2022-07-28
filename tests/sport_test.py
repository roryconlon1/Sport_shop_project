import unittest
from models.sport import Sport

class TestSport(unittest.TestCase):

    def setUp(self):
        self.sport = Sport("football")

    def test_sport_has_name(self):
        self.assertEqual("football", self.sport.name)