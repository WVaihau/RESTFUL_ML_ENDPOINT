import unittest
from app import app
import model as md

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_classifier(self):
        response = self.app.get('/classify', query_string = md.classifier_param)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["prediction"], "Pullover")


if __name__ == '__main__':
    unittest.main()