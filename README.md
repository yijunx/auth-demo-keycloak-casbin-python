# auth-demo-keycloak-casbin-python
This is a demo with keycloak, the casbin python is tested with mongodb

# setup the infra

* open this in the vscode devcontainer, then you will have below services running
    * keycloak
    * postgres for the keycloak
    * mongodb
    * mongoexpress to check mongodb (well can also run this outside)
    * and this app where code is written to play with casbin, keycloak to simulation kinds of authentication and authorization scenarios

# run an external pdadmin4 to take a closer look at the keycloak tables

```bash
docker run -p 8319:80 \              
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' \
    -d dpage/pgadmin4
```

Then we can inspect the gateway ip address of the postgres container:

```bash
docker inspect 520d665e3be8 | grep Gateway
```

We use the gateway ip because the pdadmin4 is running outside the bridge network of the docker-compose microservices

# setup the keycloak
