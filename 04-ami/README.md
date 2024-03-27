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

With database from the previous tutorial set, we will move to a more managable 
setup using "docker compose" to orchestrate containers for us.

## Git repository

Update your git repository with a new branch.

In this branch, implement changes and when done with testing, merge it with main.

## Set up two interconnected containers

Follow these steps in order to make a simple VoIP service based on Asterisk PBX
with PostgreSQL database as backend up and running:

1. Create a skeleton "compose.yaml" file for docker compose that will include Asterisk and Postgres
1. Set up database so it can be used by Asterisk to provision accounts
1. Configure PJSIP realtime in Asterisk and test it.

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

### Docker Compose

```bash
# build containers defined in compose.yaml file
docker compose build
# start containers
docker compose start
# build and start containers
docker compose up
```

### PSQL

```
# list all databases
\l
# list (describe) all tables in current database
\d
# decribe database table
\dt
# connect to another database
\c <database-name>
# quit psql
\q
```

### Example SQL commands for PJSIP realtime

```sql
insert into ps_aors (id, max_contacts) values (20, 3);
insert into ps_auths (id, auth_type, password, username) values (20, 'userpass', 20, 20);
insert into ps_endpoints (id, aors, auth, context, disallow, allow, direct_media) values (20, '20', '20', 'from-internal', 'all', 'alaw', 'no');
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
