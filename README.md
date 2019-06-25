# Docker Playground for Python

- [Docker Playground for Python](#Docker-Playground-for-Python)
  - [Process](#Process)
  - [Prerequisites](#Prerequisites)
    - [Building](#Building)
    - [Connecting](#Connecting)
  - [TODO](#TODO)
  - [Authors & Contributors](#Authors--Contributors)

This repository is an example running a Docker development environment for Python with a couple of handy scripts to help with building the image and connecting a running container for development purposes.

## Process

Currently the idea behind the structure of this project is to write and develop any scripts for the application you may be working on inside of the `lib/` folder. We do it this way as when we build our Docker image the `Dockerfile` tells Docker to copy over all files and folders from `lib/` plus the `requirements.txt` file in the root directory of the project, to a directory called `app/` on the newly built container. Following the previous steps the current `Dockerfile` is set to run a sample script during the build process, it only prints the platform on which the image is on but this is useful is during or just after a build you may need to run a script which isn't the application itself you're trying to host in the container.

An example for running an application with the `CMD` command in a Dockerfile is currently not included in this repository but I want to add a sample "Hello World" Flask app for demonstration purposes.

## Prerequisites

- Python 3
- Docker

### Building

To build an image simply open a terminal, navigate to where this project is located on your machine and run the following commands.

```shell
python build.py

# Output
Input the tag you would like to give the image:
```

### Connecting

To connect to an image, like building one you can use the provided script to connect to one. Simply open a terminal, navigate to where this project is located on your machine and run the following commands.

```shell
python connect.py

# Output
Input the name/tag given to the image you would like to connect to: <insert image name>
Would you like to connect to a Python or Shell instance inside this image, [py/sh]? <py/sh>
```

Once connected to the container you can then use the shell or python interpreter as per usual except now you're in a containerized environment which is great as now you can take this development image with you to other systems and platforms that run Docker and still have it work without trouble. 

_Please note I have not tested this on any other platform apart from Linux at this point in time._

## TODO

- [ ] Add "Hello World" Flask app
- [ ] Improve and clean python scripts

## Authors & Contributors

Jacob Swan-Mearns: [sWiZZleee](https://github.com/swizzleee)

Please feel free to send feedback, raise an issue, suggest something you'd like to see or contribute yourself via a Pull Request.