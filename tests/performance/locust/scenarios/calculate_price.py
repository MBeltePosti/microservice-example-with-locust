from base_user import BaseUser
from locust import task, tag


class CalculatePriceUser(BaseUser):
    abstract = True

    @task
    @tag("pricing", "feature", "load")
    def calculate_price(self):
        # The users exist already in example_data.py of the microservice, so we are not creating new ones.
        payload = {"customers": ["customer_1", "customer_2"]}

        with self.post(
            "/calculate_price",
            json=payload,
            name="POST /calculate_price",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status code: {response.status_code}")
                return

            try:
                data = response.json()
                if not isinstance(data, dict) or "price" not in data:
                    response.failure("Missing 'price' field in response")
                elif "customers" not in data or len(data["customers"]) == 0:
                    response.failure("Customer list missing or empty in response")
                else:
                    response.success()
            except Exception as e:
                response.failure(f"Invalid JSON returned: {e}")
