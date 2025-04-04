from base_user import BaseUser
from locust import SequentialTaskSet, task, HttpUser
from utils.tag_helper import tag_all_tasks
import uuid
import random


@tag_all_tasks("crud", "smoke", "baseline")
class CustomerCRUDFlow(SequentialTaskSet):

    def on_start(self):
        self.customer_id = None
        self.payload = {
            "name": f"Test User {uuid.uuid4()}",
            "email": f"user{random.randint(1000,9999)}@example.com",
            "price": random.randint(10, 100),
        }

    @task
    def create_customer(self):
        with self.user.post(
            "/customers",
            json=self.payload,
            name="POST new customer",
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                try:
                    data = response.json()
                    self.customer_id = data.get("customer_id")
                    if not self.customer_id:
                        response.failure("No customer_id returned")
                    else:
                        response.success()
                except Exception as e:
                    response.failure(f"Invalid JSON on create: {e}")
            else:
                response.failure(f"Failed to create customer: {response.status_code}")

    @task
    def get_customer(self):
        if not self.customer_id:
            return
        with self.user.get(
            f"/customers/{self.customer_id}",
            name="GET created customer",
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Could not fetch created customer")

    @task
    def update_customer(self):
        if not self.customer_id:
            return
        update_payload = {"name": "Updated User"}
        with self.user.put(
            f"/customers/{self.customer_id}",
            json=update_payload,
            name="PUT (update) created customer",
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Customer update failed")

    @task
    def delete_customer(self):
        if not self.customer_id:
            return
        with self.user.delete(
            f"/customers/{self.customer_id}",
            name="DELETE created customer",
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Customer deletion failed")

        self.interrupt()


class CustomerCRUDUser(BaseUser):
    tasks = [CustomerCRUDFlow]
