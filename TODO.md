# ✅ Test Automation Framework Setup – Task List

This checklist defines the step-by-step tasks to build a Dockerized performance and functional test framework using Locust and Robot Framework, targeting a sample microservice. This todo list was generated after asking ChatGPT ideas what I wanted to achieve, as such it may not represent the perfect sequence of tasks but it does aid in working towards creation of more complex ideas.

---

## 🧱 Phase 1: Microservice Setup

- [✅] Fork and clone [`ebroda/microservice-python-example`](https://github.com/ebroda/microservice-python-example)
- [✅] Run the microservice locally and verify it's working
- [✅] Create a `Dockerfile` for the microservice (if missing)
- [✅] Expose the correct port (e.g., 5000) - Did it with 4999.
- [✅] Add basic `/health` endpoint (if not present)
- [✅] Run microservice container standalone (`docker run ...`)

---

## 🧪 Phase 2: Locust Performance Framework

- [✅] Create `/tests/performance/locust/` folder
- [✅] Add a simple `basic_smoke_test.py` hitting one endpoint
- [✅] Add `requirements.txt` for Locust dependencies
- [✅] Create a `Dockerfile` for the Locust image
- [✅] Create `docker-compose.yml` with:
  - [✅] 1 Locust master
  - [✅] 3 Locust workers
- [✅] Configure environment variables to pass microservice host
- [✅] Add example `README.md` explaining how to run Locust locally

---

## 🚦 Phase 3: Scenario Design & CI Pipeline

- [✅] Add `HealthCheckUser` to test `GET /health`
- [✅] Add `GetAllCustomersUser` → tests `GET /customers`
- [✅] Add `CustomerCRUDUser`:
  - [✅] `POST /customers` to create a new customer
  - [✅] `GET /customers/<id>` to retrieve the customer
  - [✅] `PUT /customers/<id>` to update the customer
  - [✅] `DELETE /customers/<id>` to delete the customer
- [✅] Add `MagicEndpointUser` → tests `POST /do_your_magic`
- [✅] Add `CalculatePriceUser` → tests `POST /calculate_price` with valid customer data
- [ ] Add `.github/workflows/perf-test.yml` GitHub Actions pipeline:
  - [ ] Spin up microservice container
  - [ ] Run Locust in headless mode for selected test users
  - [ ] Save or print Locust stats as CI artifacts

---

## 🤖 Phase 4: Robot Framework Integration

- [ ] Add GET and POST API tests using `/customers` and `/calculate_price`
- [ ] Add negative tests (e.g., missing fields, non-existent customer ID)
- [ ] Create `LocustRunner.py` or keyword resource file:
  - [ ] Keyword to start Locust test run
  - [ ] Keyword to wait for test result
  - [ ] Keyword to assert on thresholds
- [ ] Capture and report Locust results in Robot logs or external file

---

## 🔧 Phase 5: Orchestration & Local UX

- [ ] Create root-level `docker-compose.yml` to orchestrate:
  - [ ] Microservice container
  - [ ] Locust master + 3 workers
  - [ ] Robot Framework container
- [ ] Use `.env` file for flexible config
- [ ] Add `Makefile` or shell scripts:
  - [ ] `make up` → launch all
  - [ ] `make test` → run tests
  - [ ] `make clean` → teardown everything

---

## 📊 Phase 6: Optional Live Monitoring

- [ ] Integrate Portainer or Dockprom for live container dashboard
- [ ] Allow real-time container interaction visualization
- [ ] Document how to use optional monitoring tools

---

## 📝 Phase 7: Documentation

- [ ] Write top-level `README.md` including:
  - [ ] Project purpose
  - [ ] Locust usage guide (local and Docker)
  - [ ] Robot Framework usage guide
  - [ ] Docker-based test orchestration guide
  - [ ] CI/CD integration details
  - [ ] How to interpret results and extend tests