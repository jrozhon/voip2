# Environment

There are virtual computers available. The IP addresses (available from a
private network in laboratory only) are: **10.100.0.41-53**.

The credentials are as usual:

- username: **student**
- password: **student**
- root access via **sudo**

# Agenda

In this tutorial, we are going to implement a core of a VoIP testbed consisting
of Asterisk PBX servers.

Requirements:

- general knowledge of SIP/SDP/RTP protocols and related services
- bash scripting
- docker
- git

Steps to follow:

- create a github repository for your project
- prepare a docker container serving Asterisk PBX
- configure accounts on Asterisk PBX:
  - 10
  - 11
- test the connectivity and audio transmission
- connect your PBX to the network (trunk)

## Git repository

Throughout the course we are going to store the progress in the git repository
to allow for easy version control of our configuration.

1. Set up an account on github.com
2. Create a github repository called **my-voip2**
3. Add a README.md and .gitignore files

## Set up a simple docker container for Asterisk PBX

Follow these steps in order to make a simple VoIP service based on Asterisk PBX
up and running:

1. Use [debian image](https://hub.docker.com/_/debian) as a starting point and
   create a container for Asterisk PBX. Consult with
   [Docker reference](https://docs.docker.com/engine/reference/builder/) for
   instruction on how to structure Dockerfile.
1. Accomodate the requirements of Asterisk PBX on a given platform (no binaries,
   etc.).
1. Consider the requirements of network configuration (open ports, etc.).
   Consult Docker reference for port utility functions - EXPOSE and PUBLISH.
1. Provision a simple configuration that would allow client devices (phones) to
   connect to the server and make a phone call. Use accounts 10 and 11.
1. Inspect the communication in:
   1. CLI of Asterisk PBX,
   1. Trace of signalling and media communication.

## Useful commands

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
docker run -d --name asterisk -p 5060:5060/udp -p 10000-10100:10000-10100/udp jrozhon/asterisk
# Connect to container
docker exec -it asterisk /bin/bash
# remove container
docker container rm asterisk
```
