from base_user import BaseUser
from locust import task, tag


class HealthCheckUser(BaseUser):

    @tag("sanity", "health")
    @task
    def health_check(self):
        self.get("/health", name="Health Check")
