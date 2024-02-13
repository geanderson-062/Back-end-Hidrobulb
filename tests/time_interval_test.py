import unittest
import requests


class TestAPIIntegration(unittest.TestCase):
    base_url = "http://127.0.0.1:8000"

    def test_time_interval_endpoint(self):
        response = requests.get(f"{self.base_url}/time_interval")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
