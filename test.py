import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.base_url = 'http://127.0.0.1:5000'

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Вычисление тригонометрических функций'.encode('utf-8'), response.data)

    def test_about_page(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Об авторе'.encode('utf-8'), response.data)
        self.assertIn('Пьянникова Елизавета Андреевна'.encode('utf-8'), response.data)
        self.assertIn('Группа: ПИН-231'.encode('utf-8'), response.data)
        self.assertIn('Факультет: ФИТИКС'.encode('utf-8'), response.data)

    def test_valid_input(self):
        response = self.app.post('/', data={'angle': 45, 'precision': 2, 'units': 'degrees'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Результат'.encode('utf-8'), response.data)

    def test_empty_field_error_message(self):
        response = self.app.post('/', data={'angle': None, 'precision': None, 'units': ''})
        self.assertEqual(response.status_code, 400)

    def test_noAngle_field_error_message(self):
        response = self.app.post('/', data={'angle': None, 'precision': "5", 'units': 'degrees'})
        self.assertEqual(response.status_code, 400)

    def test_noPrec_field_error_message(self):
        response = self.app.post('/', data={'angle': "60", 'precision': None, 'units': 'degrees'})
        self.assertEqual(response.status_code, 400)

    def test_noUnits_field_error_message(self):
        response = self.app.post('/', data={'angle': "60", 'precision': "6", 'units': None})
        self.assertEqual(response.status_code, 400)

    def test_ancorrectPres_field_error_message(self):
        response = self.app.post('/', data={'angle': "60", 'precision': "0.0001", 'units': 'degrees'})
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()