# orodha-deployment

This repository contains the scripts and configuration that are necessary in order to run and deploy the Orodha application.

## Docker-compose file

The docker-compose file creates each of our services with their associated database, as well as our NGINX container that is accessible on port 80.

### Container Environment Variables

The docker-compose.yaml file consumes variables related to each service's db user as well as the root db user.

The variables are as follows:

- DBROOTUSER
- DBROOTPASSWORD
- NOTIFICATIONDBUSER
- NOTIFICATIONDBPASSWORD
- NOTIFICATIONDBNAME
- USERDBUSER
- USERDBPASSWORD
- USERDBNAME
- LISTDBUSER
- LISTDBPASSWORD
- LISTDBNAME

You can feed these variables in by using the --env-file flag on the docker-compose command like so:

`docker-compose -f docker-compose.main.yaml --env-file orodha.env`

## orodha-base-image

The orodha-base-image folder contains a Dockerfile, a script called
`build-and-push.sh`, and two separate requirements.txt files.

The Dockerfile outlines an image that comes from python:3.11.4-alpine3.18 and simply sets up the environment for the greatest common denominater requirements for each of our flask-restx services.

You can use the --build-arg flag with the docker build command in order to set which requirements.txt file is used to build the base. This way, in our CI/CD pipeline we can pull our image built with the dev-requirements.txt, called `edisonstuart/orodha-base-image-dev/{tag}`, in order to test that everything is working as intended; then, pull our image that has been built with the prod-requirements.txt file, called `edisonstuart/orodha-base-image-prod/{tag}`, that we eventually will be pushing to AWS.

### Build Environment Variables

the `build-and-push.sh` file expects two values, and has two more optional values. These values are as follows:

#### required

- DOCKER_USERNAME
  flag -u
- DOCKER_PASSWORD
  flag -p

#### optional

- BUILD_TAG
  flag -t
- LAUNCH_OPTION
  flag -L (lowecase)

## scripts

The scripts folder contains three `db.js` scripts that create our three mongo users for each of our services. These scripts are what consume the previously mentioned [Container Environment Variables](#container-environment-variables) and are mounted as a volume into the `docker-entrypoint-initdb.d` directory.

## Config Directory

The config directory contains some simple configuration for NGINX that allows it to act as a reverse proxy for our application. This whole folder is mounted into etc/nginx/conf.d in the NGINX container instead of the default config.

The `server.conf` file contains some simple configuration that determines some basic information about the server such as server name and port. The file also contains an include statement that allows us to pull in our files under the proxy_config directory.

### proxy_config

The files under proxy_config are `list.conf`, `notification.conf`, and `user.conf`. These files each contain a simple location block structured like so:

```
location ~ /{path} {
    rewrite /{path}(.*) /api/v1$1 break;
    proxy_pass http://{service}-service-server:5000;
}
```

`{path}` and `{service}` being variables based on the service.
