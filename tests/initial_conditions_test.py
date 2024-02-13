import unittest
import requests


class TestAPIIntegration(unittest.TestCase):
    base_url = "http://127.0.0.1:8000"

    def test_initial_conditions_endpoint(self):
        response = requests.get(f"{self.base_url}/initial_conditions/norte")
        self.assertEqual(response.status_code, 200)

    def test_initial_conditions_nordeste_endpoint(self):
        response = requests.get(f"{self.base_url}/initial_conditions/nordeste")
        self.assertEqual(response.status_code, 200)

    def test_initial_conditions_centro_oeste_endpoint(self):
        response = requests.get(f"{self.base_url}/initial_conditions/centro_oeste")
        self.assertEqual(response.status_code, 200)

    def test_initial_conditions_sudeste_endpoint(self):
        response = requests.get(f"{self.base_url}/initial_conditions/sudeste")
        self.assertEqual(response.status_code, 200)

    def test_initial_conditions_sul_endpoint(self):
        response = requests.get(f"{self.base_url}/initial_conditions/sul")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
