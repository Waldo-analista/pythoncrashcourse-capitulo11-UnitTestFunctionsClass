import unittest
from city_functions import ciudad_pais

class TestUnit(unittest.TestCase):
    def test_ciudad_pais(self):
        ciudadpais=ciudad_pais('santiago','chile')
        self.assertEqual(ciudadpais,'Santiago, Chile')
    def test_ciudad_pais_population(self):
        ciudad_pais_population=ciudad_pais('santiago','chile',5000000)
        self.assertEqual(ciudad_pais_population,'Santiago, Chile- population 5000000')

unittest.main()