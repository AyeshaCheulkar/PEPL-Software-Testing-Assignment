import os
import requests
class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv(
            "BASE_URL",
            "http://localhost:3001"
        )
        self.session = requests.Session()
    def get(self, endpoint, **kwargs):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            **kwargs
        )
    def post(self, endpoint, **kwargs):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            **kwargs
        )
    def put(self, endpoint, **kwargs):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            **kwargs
        )
    def patch(self, endpoint, **kwargs):
        return self.session.patch(
            f"{self.base_url}{endpoint}",
            **kwargs
        )
    def delete(self, endpoint, **kwargs):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            **kwargs
        )
