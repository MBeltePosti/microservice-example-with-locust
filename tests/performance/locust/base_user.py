from locust import HttpUser, between
from config import TARGET_HOST


class BaseUser(HttpUser):
    abstract = True
    wait_time = between(1, 2)
    host = TARGET_HOST

    headers = {"User-Agent": "performance-tester", "Accept": "application/json"}

    def get(self, path, **kwargs):
        return self.client.get(path, headers=self.headers, **kwargs)

    def post(self, path, data=None, **kwargs):
        return self.client.post(path, data=data, headers=self.headers, **kwargs)

    def put(self, path, data=None, **kwargs):
        return self.client.put(path, data=data, headers=self.headers, **kwargs)

    def delete(self, path, **kwargs):
        return self.client.delete(path, headers=self.headers, **kwargs)
