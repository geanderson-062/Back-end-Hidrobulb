import unittest
import requests


class TestAPIIntegration(unittest.TestCase):
    base_url = "http://127.0.0.1:8000"

    def test_soil_properties_norte_endpoint(self):
        response = requests.get(f"{self.base_url}/soil_properties/norte")
        self.assertEqual(response.status_code, 200)

    def test_soil_properties_nordeste_endpoint(self):
        response = requests.get(f"{self.base_url}/soil_properties/nordeste")
        self.assertEqual(response.status_code, 200)

    def test_soil_properties_centro_oeste_endpoint(self):
        response = requests.get(f"{self.base_url}/soil_properties/centro_oeste")
        self.assertEqual(response.status_code, 200)

    def test_soil_properties_sudeste_endpoint(self):
        response = requests.get(f"{self.base_url}/soil_properties/sudeste")
        self.assertEqual(response.status_code, 200)

    def test_soil_properties_sul_endpoint(self):
        response = requests.get(f"{self.base_url}/soil_properties/sul")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
