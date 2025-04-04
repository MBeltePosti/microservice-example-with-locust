# for purposes of learning, a microservice example with locust

The forked microservice is at the root with small changes. 
The Locust tests are in tests/performance/locust.

docker-compose.yml is set up for sole purpose of launching microservice container, then launch Locust Master container and three Locust worker containers. Idea being to demonstrate scaling of the locust performance tests in distributed set up. Each container could be easily placed in their own servers.

# Starting
Locally using Docker you can start microservice and launch locust using: 

    docker-compose up --build

Running it on GitHub Actions there is .github/workflows/perf-test.yml. This workflow will start the microservice and execute tests in headless mode using command overrides defined there. I didn't add more complexity to it since gthat wasn't the overarching goal of this exercise.
In real life we may not want to do all of this in a single workflow file, launching and running inside GitHub Actions. After all, performance tests should be executed against real environment with specific goals. 

Also we would benefit from versioning.

# microservice-python-example
A small example of a REST like microservice written in python

The example is based on the flask library. 
Documentation can be found under: http://flask.pocoo.org/docs/1.0/

It implements the basic REST routes for an example customer resource.

    GET / : Welcome Message
    GET /customers : Retrieve all customers
    GET /customers/<customer_id> : Retrieve a single customer resource
    PUT /customers/<customer_id> : Update a single customer resource
    DELETE /customers/<customer_id> : Delete a single customer resource
    POST /customers : Create a new customer resource
    
    POST /do_your_magic: Barebone example for a simple service
    POST /calculate_price: (Simple) example for a possible price calculation
    GET /health: check health

Additionally there is a endpoint called "do_your_magic" as an barebone example on how to implement a simple service.

# Dockerfile
The example can be easily deployed and tested using docker.
Just install docker and execute the following commands.

    $ docker build . -t python-microservice-example
    $ docker run --name python-microservice-example_1 -d -p 5000:5000 python-microservice-example

After the docker container is up and running you will be able to access the microservice via HTTP calls.
Go to your browser and enter: http://localhost:5000/customers
You should now see a list of example customer resources.

I recommend to use POSTMAN (https://www.getpostman.com/) to test the other methods, like POST, PUT and DELETE
You will find a postman_collection.json file next to the other sources, that you can import into POSTMAN.
