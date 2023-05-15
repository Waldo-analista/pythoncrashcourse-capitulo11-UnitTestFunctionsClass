import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_primer_ultimo_nombre(self):
        full_name=get_formatted_name('waldo','hidalgo')
        self.assertEqual(full_name,'Waldo Hidalgo')
    def test_primer_medio_ultimo_nombre(self):
        full_name=get_formatted_name('waldo','oyarce','hidalgo')
        self.assertEqual(full_name,'Waldo Hidalgo Oyarce')



unittest.main()
