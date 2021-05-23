# set base image (host OS)
FROM alpine:3.13

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN apk add python3 gcc python3-dev py3-pip musl-dev
RUN pip3 install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python3", "mconBot.py" ]
