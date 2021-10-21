#contains instructions about building the application image
# we start from some base image and install required dependencies
# e.g. For django project we will need to install python, django, virtual
# environment.
# Add instruction to activate virtual envoronment,
# install required packages and run the django application
# Also add instructions to install database, start database,
# At the end the image is build and can be push to docker repository
# once the image is run in a container, it becomes easy to scale as we
# we will have to copy the same image and run in any number of containers.

#FROM python:3
FROM polling_app_web
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

