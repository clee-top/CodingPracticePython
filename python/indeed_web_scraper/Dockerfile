FROM ubuntu:16.04

# Example build commmand:
# docker build -t indeed-scraper:latest .

#Example run command:
#  -d detaches the container and runs in the background which is great since it's a web server and we want it to
#  sit around listening for calls to it passively.
#  -p 5000:5000 links the host port 5000 to docker port 5000 so we can make calls to this thing to our host as if
#  it was running locally.
# "docker run -d -p 5000:5000 indeed-scraper:latest"

MAINTAINER Chris Lee "topagae@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install --upgrade pip

# Copy the requirements.txt first to leverage Docker cache. Then the two python files we need.
COPY requirements.txt /app/requirements.txt

# Usually good practice not to use root as workdir.
WORKDIR /app

# Install the things we need to run the app.
RUN pip install -r requirements.txt

# Copy everything else into the app. Should get us our two python files, readme and test data.
COPY . /app

ENTRYPOINT ["python"]

CMD ["scrape_app.py"]
