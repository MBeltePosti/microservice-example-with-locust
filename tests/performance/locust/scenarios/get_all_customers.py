from base_user import BaseUser
from locust import task, tag


class GetAllCustomersUser(BaseUser):
    @tag("customers", "baseline")
    @task
    def get_customers(self):
        with self.get(
            "/customers",
            name="Get all customer data at once from imaginary db",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status code: {response.status_code}")
                return
            try:
                data = response.json()
                if isinstance(data, list) and len(data) > 0:
                    response.success()
                else:
                    response.failure("Empty or invalid customer list")
            except Exception as e:
                response.failure(f"Invalid JSON: {e}")
