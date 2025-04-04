# 🐛 Locust Performance Tests (Docker Setup)

This folder contains Dockerized performance tests for the microservice, using Locust in distributed mode (1 master + 3 workers).
Distributed mode means that Master is overseeing Workers that actually perform the tests, this is useful in cases where we need to distribute the performance tests. Containers are perfect for this because you can create as many workers as needed to be launched in any server you need.

---

## Depends on

This framework is part of a sample microservice to be run in isolation from other services. To have service running locally as you run these Locust tests, use docker-compose.yml in project root directory. This file has defined what containers will be brought up, including master and workers.
You can also run this Locust framework without container locally, for that instructions are not provided in this readme and will be done later.

## 🚀 Run Locust with Docker Compose

From the **project root**, run:

```bash
docker-compose up --build
```

> Make sure a `.env` file exists in the root directory with the target microservice URL:

```env
TARGET_HOST=http://microservice:4999
```

---

## 🌐 Access Locust UI

Once running, open:

[http://localhost:8089](http://localhost:8089)

You can start your test by entering:
- Number of users
- Spawn rate
- Host (automatically prefilled from `TARGET_HOST`)

## 🤖 For Headless Mode

Modify docker-compose.yml locust-master container command to something like:

```bash
command: >
  locust -f run_all.py
  --master
  --headless
  -u 10 -r 2 --run-time 1m
  --host=${TARGET_HOST}
```

or override with command when executing docker-compose.yml:

```bash
docker-compose run --rm locust-master \
  locust -f run_all.py \
  --master --headless \
  -u 10 -r 2 --run-time 1m \
  --host=${TARGET_HOST}
```

- -u 10: 10 users
- -r 2: hatch rate (2 users/sec)
- --run-time 1m: run for 1 minute

You can also run locust in not distributed mode (without master and workers) but instructions for that are not here provided.

---

## 🏷️ Tags

- `sanity` – basic availability checks
- `smoke` – happy path flows
- `baseline` – full release tests
- `crud`, `pricing`, `magic`, `health`, `customers` – specific features

## 📁 Project Structure

```
tests/performance/locust/
├── scenarios/
│   ├── health_check.py   # Checks if service is healthy. Not mandatory for performance tests since user is not going to interact with this endpoint.
│   ├── get_all_customers.py  # It's possible that in real life there is something that requests listing all users in the system so that's what it tests.
│   ├── customer_crud.py  # Most common scenario for a REST microservice that deals with creating, updating and deleting data.
│   ├── magic_endpoint.py  # This sample microservice came with this endpoint but it doesn't do anything special, covered it anyway.
│   └── calculate_price.py  # There is a small calculation in the service so we cover that feature as well.
├── base_user.py
├── config.py
├── requirements.txt
├── Dockerfile
├── README.md
└── run_all.py  # Entry point to execute all test scenarios in performance test in a single run. This is not always needed and should be treated as optional.
```

---

## 🛠️ Notes

- Locust runs in **distributed mode** (1 master, 3 workers)
- Host URL is set via the `TARGET_HOST` variable in `.env` or Compose
- Use `Ctrl+C` to stop containers
