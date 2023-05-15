import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question='¿Qué lenguaje de programación aprendiste primero?'
        self.encuesta=AnonymousSurvey(question)
        self.responses=['Java','Python','JavaScript']


    def test_store_single_response(self):
        self.encuesta.store_response(self.responses[0])
        self.assertIn('Java',self.encuesta.responses)
    
    def test_store_three_responses(self):
        for lenguaje in self.responses:
            self.encuesta.store_response(lenguaje)
        for response in self.responses:
            self.assertIn(response,self.encuesta.responses)



unittest.main()