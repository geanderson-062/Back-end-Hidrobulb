import unittest
import requests


class TestAPIIntegration(unittest.TestCase):
    base_url = "http://127.0.0.1:8000"

    def test_saturation_drainage_norte_endpoint(self):
        response = requests.get(f"{self.base_url}/saturation_drainage/norte")
        self.assertEqual(response.status_code, 200)

    def test_saturation_drainage_nordeste_endpoint(self):
        response = requests.get(f"{self.base_url}/saturation_drainage/nordeste")
        self.assertEqual(response.status_code, 200)

    def test_saturation_drainage_centro_oeste_endpoint(self):
        response = requests.get(f"{self.base_url}/saturation_drainage/centro_oeste")
        self.assertEqual(response.status_code, 200)

    def test_saturation_drainage_sudeste_endpoint(self):
        response = requests.get(f"{self.base_url}/saturation_drainage/sudeste")
        self.assertEqual(response.status_code, 200)

    def test_saturation_drainage_sul_endpoint(self):
        response = requests.get(f"{self.base_url}/saturation_drainage/sul")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
