# Environment

There are virtual computers available. The IP addresses (available from a
private network in laboratory only) are: **10.100.0.41-53**.

The credentials are as usual:

- username: **student**
- password: **student**
- root access via **sudo**

# Agenda

Based on the previous tutorial, we are going to update the current infrastructure 
to include services, such as conferences and voice menus.

As an optimization, we are also going to change our docker file for Asterisk PBX 
to employ two-stage build and observe the difference in image size.

Lastly, a second container with PostgreSQL will be build and tested for connectivity.

## Git repository

Update your git repository with a new branch (after you set up 2 extensions successfully).

In this branch, implement changes and when done with testing, merge it with main.

## Set up a simple docker container for Asterisk PBX

Follow these steps in order to make a simple VoIP service based on Asterisk PBX
up and running:

1. Link individual nodes together to the SIP network.
1. Experiment with the setup of more advanced services, such as IVR and Conferences.
1. Use [postgresql image](https://hub.docker.com/_/postgres) as a container for  
   PostgreSQL database.

## Useful commands

### Docker

```bash
# list images
docker image ls
# list containers
docker ps
# or
docker container ls
# Build image from dockerfile
docker build -t jrozhon/asterisk .
# Run container from image
docker run -d --name asterisk -p 5060:5060/udp -p 10000-10100:10000-10100/udp -v $(pwd)/asterisk:/etc/asterisk jrozhon/asterisk
# Connect to container
docker exec -it asterisk /bin/bash
# remove container
docker container rm asterisk
# use predefined container
docker run --name postgres -e POSTGRES_PASSWORD=postgres -d postgres
# clear system
docker system prune -a
# check the logs of a container asterisk
docker logs asterisk
# copy files between filesystem and container
docker cp asterisk:/etc/asterisk .
```

### Asterisk

```bash
# connect to asterisk console
asterisk -vvvvvvvvvvvvvvvvvr
# check pjsip endpoints
pjsip show/list endpoints
# check specifi endpoint
asterisk show endpoint 10
# check pjsip transports
pjsip show/list transports
# check asterisk modules
module show like pjsip
# check asterisk dialplan
dialplan show
# restart asterisk from asterisk cli
core restart now
```
