from base_user import BaseUser
from locust import task, tag


class MagicEndpointUser(BaseUser):
    """Magic endpoint user for testing the /do_your_magic endpoint. This endpoint in sample microservice is used to provide example if there was an endpoint with async method call. We're including it in performance tests just to cover all endpoints"""

    @tag("magic", "feature", "stress")
    @task
    def call_magic(self):
        payload = {"input": "meaningless payload", "energy": "average"}

        with self.post(
            "/do_your_magic",
            json=payload,
            name="POST /do_your_magic",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status code: {response.status_code}")
                return

            try:
                data = response.json()
                magic_things = data.get("list_of_magic_things", [])
                if not isinstance(magic_things, list) or len(magic_things) < 1:
                    response.failure("Missing or empty magic things list")
                else:
                    response.success()
            except Exception as e:
                response.failure(f"Invalid JSON: {e}")
