# Nautobot Docker Images

Nautobot is packaged as a docker image for use in a production environment.  The published image is based on the `python:3.6-slim` docker image to maintain the most compatibility with Nautobot deployments.  The docker image and deployment strategies are being actively developed, check back here or join the **#nautobot** Slack channel on [Network to Code](https://networktocode.slack.com) for the most up to date information.

## Tags

We publish the docker image to both the Github container registry as well as docker hub.  The image can be pulled with either:

```
docker image pull networktocode/nautobot
docker image pull ghcr.io/nautobot/nautobot
```

The following tags are available:

* `vX.Y.Z` these images are built with the same baseline as the released Python packages
* `latest` these images are built from the latest code in the main branch (should be the latest released version)
* `latest-dev` these images are built from the latest code in the develop branch on each commit
* `develop-${GIT_SHA:0:7}-$(date +%s)` tags for each commit to the develop branch

## Getting Started

Nautobot requires a Postgres database and Redis cache before it will start, because of this the quickest and easiest way to get Nautobot running is with docker-compose.  Please see the docker-compose deployment repository for more information.

## Configuration

Most configuration parameters are available via environment variables which can be passed to the container.  If you desire you can inject your own `nautobot_config.py` by overriding `/opt/nautobot/nautobot_config.py`.

### SSL

Self signed SSL certificates are included by default with the container.  For a production deployment you should utilize your own signed certificates, these can be injected into the container at runtime.  The public certificate should be placed at `/opt/nautobot/nautobot.crt` and the private key should be at `/opt/nautobot/nautobot.key`.

### Plugins

At this time adding plugins to the existing docker image is not supported, however, you can use this docker image as the base for your Dockerfile to install your own plugins:

## Building the Image

If you have a [development environment](/development/getting-started/#setting-up-your-development-environment) you can use invoke to build the docker images.  By default `invoke build` will build the development containers:

```
$ invoke build
...
$ docker images
REPOSITORY                                                                TAG                    IMAGE ID       CREATED          SIZE
networktocode/nautobot-dev                                                local                  25487d93fc1f   16 seconds ago   630MB
```

If you need to build/test the final image set the `OVERRIDE_FILENAME`:

```
$ export OVERRIDE_FILENAME=docker-compose.test.yml
$ invoke build
...
$ docker images
REPOSITORY                                                                TAG                    IMAGE ID       CREATED          SIZE
networktocode/nautobot                                                    local                  0a24d68da987   55 seconds ago   337MB
```

If you do not have a development environment created you can also build the container using the regular `docker build` command:

```
$ docker build -t networktocode/nautobot -f ./docker/Dockerfile --build-arg PYTHON_VER=3.6 .
```