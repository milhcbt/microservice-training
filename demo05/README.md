# Demo 05
## Description
This demo is a simple web application that uses 3 application to display a web page with a greeting, the current time, and the name of the host(user). 
this version of demo contain 3 application, hello in python, world in java and time in golang. all tree application will be run in docker container, and we will use docker-compose to run all of them.
each application accessed through traefik reverse proxy, so we can access all application through one port.

Traefik is an open-source Edge Router that makes publishing your services a fun and easy experience. It receives requests on behalf of your system and finds out which components are responsible for handling them. Traefik role on micrservice architecture is as reverse proxy, so we can access all application through one port.

## Requirement
- Docker and Docker Compose, tested with Docker version 20.10.8, build 3967b7d and docker-compose version 1.29.2
- Images for each application, see Dockerfile in each application folder for more detail.

## Run.
- before run this demo, make sure you have docker and docker-compose installed in your machine.
- create network called `web` for traefik reverse proxy to communicate with other application
```bash
docker network create web
```
- run all application using docker-compose
```bash
docker-compose up -d
```
- open browser and go to http://localhost/hello or http://localhost/world or http://localhost/time
- to stop all application
```bash
docker-compose down
```
- to stop all application and remove all container
```bash
docker-compose down --rmi all
```
- to stop all application and remove all container and volume
```bash
docker-compose down --rmi all --volumes
```
- to stop all application and remove all container and volume and network
```bash
docker-compose down --rmi all --volumes --remove-orphans
```
- to follow log of all application
```bash
docker-compose logs -f
```
- to follow log of specific application
```bash
docker-compose logs -f <application_name>
```
- to access shell of specific application
```bash
docker-compose exec <application_name> sh
```
- to see status of all application
```bash
docker-compose ps
```
- to see status of specific application
```bash
docker-compose ps <application_name>
```

Complete docker-compose command can be found [here](https://docs.docker.com/compose/reference/overview/)

here ini docker-compose.yml file
```yaml
version: '3'

services:
  gateway:
    image: traefik:v2.5
    command: --configFile=/etc/traefik/traefik.yml
    volumes:
      - ./traefik.yml:/etc/traefik/traefik.yml
      - ./traefik-dynamic-conf.yml:/etc/traefik/traefik-dynamic-conf.yml
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080"
    networks:
      - web

  hello:
    build: 
      context: hello
      dockerfile: Dockerfile
    # ports:
    #   - "5000:5000"
    networks:
      - web
  world:
    build: 
      context: world
      dockerfile: Dockerfile
    # ports:
    #   - "5001:5001"
    networks:
      - web
  time:
    build: 
      context: time
      dockerfile: Dockerfile
    # ports:
    #   - "5002:5002"
    networks:
      - web

networks:
  web:
    external: true

```