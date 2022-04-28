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

* go to localhost:8080
* login with the username / password in docker-compose for keycloak
* go to top left master, then Add Realm, key in name, then create
* now create a user, in the left panel, click users, then click add user
* here i am going to create a user, after key in name and email, go to credential and setup a password
* now lets use the user to logim the Keycloak Account Console at `http://localhost:8080/auth/realms/realm_001/account/#/`, will be asked to change to a new password `password2`. This user can also change his email, first name, last name (BUT NOT USERNAME) in the personal info tab.
* at last lets secure first app, lets go back to the admin console, and select the realm.
* go to clients (left panel), then create

