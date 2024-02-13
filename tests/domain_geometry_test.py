import unittest
import requests


class TestAPIIntegration(unittest.TestCase):
    base_url = "http://127.0.0.1:8000"

    def test_domain_geometry_norte_endpoint(self):
        response = requests.get(f"{self.base_url}/domain_geometry/norte")
        self.assertEqual(response.status_code, 200)

    def test_domain_geometry_nordeste_endpoint(self):
        response = requests.get(f"{self.base_url}/domain_geometry/nordeste")
        self.assertEqual(response.status_code, 200)

    def test_domain_geometry_centro_oeste_endpoint(self):
        response = requests.get(f"{self.base_url}/domain_geometry/centro_oeste")
        self.assertEqual(response.status_code, 200)

    def test_domain_geometry_sudeste_endpoint(self):
        response = requests.get(f"{self.base_url}/domain_geometry/sudeste")
        self.assertEqual(response.status_code, 200)

    def test_domain_geometry_sul_endpoint(self):
        response = requests.get(f"{self.base_url}/domain_geometry/sul")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
