import unittest
import requests


class TestAPIIntegration(unittest.TestCase):
    base_url = "http://127.0.0.1:8000"

    def test_climate_parameters_norte_endpoint(self):
        response = requests.get(f"{self.base_url}/climate_parameters/norte")
        self.assertEqual(response.status_code, 200)

    def test_climate_parameters_nordeste_endpoint(self):
        response = requests.get(f"{self.base_url}/climate_parameters/nordeste")
        self.assertEqual(response.status_code, 200)

    def test_climate_parameters_centro_oeste_endpoint(self):
        response = requests.get(f"{self.base_url}/climate_parameters/centro_oeste")
        self.assertEqual(response.status_code, 200)

    def test_climate_parameters_sudeste_endpoint(self):
        response = requests.get(f"{self.base_url}/climate_parameters/sudeste")
        self.assertEqual(response.status_code, 200)

    def test_climate_parameters_sul_endpoint(self):
        response = requests.get(f"{self.base_url}/climate_parameters/sul")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
