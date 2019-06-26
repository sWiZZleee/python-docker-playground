# Docker Playground for Python

- [Docker Playground for Python](#Docker-Playground-for-Python)
  - [Process](#Process)
  - [Prerequisites](#Prerequisites)
  - [Building](#Building)
  - [Connecting & Running](#Connecting--Running)
  - [TODO](#TODO)
  - [Authors & Contributors](#Authors--Contributors)

This repository is an example running a Docker development environment for Python with a couple of handy scripts to help with building the image and connecting a running container for development purposes. I do understand it is maybe a bit unconventional in a sense to use Python scripts to handle the building and running of containers over say the standard shell scripting form of doing things but I selected this method as yes I may be comfortable writing bash scripts, but if I find myself needing to possibly do more elaborate tasks I would much prefer Python for such tasks. 

## Process

Currently the idea behind the structure of this project is to write and develop any scripts for the application you may be working on inside of the `lib/` folder. We do it this way as when we build our Docker image the `Dockerfile` tells Docker to copy over all files and folders from `lib/` plus the `requirements.txt` file in the root directory of the project, to a directory called `app/` on the newly built container, install the requirements then run the sample Flask app included.

  - Copy over the `lib/` directory where we developed our application
  - Copy over the `requirements.txt`
  - Install all necessary dependencies
  - Run the Application

## Prerequisites

You must have the following requirements installed.

- Python 3
- Docker

It is assumed that you have the basic knowledge of using both of these.

## Building

To build an image simply open a terminal, navigate to where this project is located on your machine and run the following commands.

```shell
# To avoid using python before all commands
# You can run "chmod +x build.py" on a UNIX system
# Now you can instead run "./build.py"
python build.py 

# Output
Input the tag you would like to give the image:
```

## Connecting & Running

To connect to an image, like building one you can use the provided script to connect to one. Simply open a terminal, navigate to where this project is located on your machine and run the following commands.

```shell
# To avoid using python before all commands
# You can run "chmod +x run.py" on a UNIX system
# Now you can instead run "./run.py"
python run.py

# Output
Input the name/tag given to the image you would like to connect to: <insert image name>
Would you like to connect to a Python or Shell instance inside this image, [py/sh/run]? <py/sh/run>

# If you selected to run an image
Input the port you want to map from the container: <port the app runs on>
Input the port which you want to map it to on your machine: <port you want to access from on your machine>
 * Serving Flask app "app" (lazy loading)
 ...
```

Once connected to the container you can then use the shell or python interpreter as per usual except now you're in a containerized environment which is great as now you can take this development image with you to other systems and platforms that run Docker and still have it work without trouble. 

_Please note I have not tested this on any other platform apart from Linux at this point in time._

## TODO

- [x] Add "Hello World" Flask app
- [ ] Improve and clean python scripts

## Authors & Contributors

Jacob Swan-Mearns: [sWiZZleee](https://github.com/swizzleee)

Please feel free to send feedback, raise an issue, suggest something you'd like to see or contribute yourself via a Pull Request.