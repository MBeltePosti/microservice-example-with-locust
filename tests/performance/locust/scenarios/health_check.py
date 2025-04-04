from base_user import BaseUser
from locust import task, tag


class HealthCheckUser(BaseUser):
    abstract = True

    @task
    @tag("sanity", "health")
    def health_check(self):
        self.get("/health", name="Health Check")
