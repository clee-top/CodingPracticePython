### This project was a take home exam given by jobr, a mobile job application site that was acquired by Monster.com. Solution works and got interview/offer.

This repository contains a Flask application running on Python 3.7 that when run serves one endpoint (/scrapeIndeed).
It expects to have json passed to it in a POST. See "driver_data.txt" for examples of this data as well as how to use
it to test the application.

The project requires the following important things be installed along with Python 3.7:
 1. Flask (http://flask.pocoo.org/)
    - Flask is an web micro framework for Python. I use it to as a simple server that responds to the one request it
    supports. 
 2. Beautiful Soup 4 (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - Beautiful Soup can take Python requests and parse them which is what I'm using to get the data I want off the 
    web pages on Indeed.com
 3. Python Requests (http://docs.python-requests.org/en/master/)
    - Python Requests is a library to send/receive HTTP requests and for this project I use it to get the raw data
    from web pages which I feed to Beautiful soup to parse for data I want.
  
You can install these libraries and its dependencies with the requirements.txt in this repository which was created with
"pip freeze > requirements.txt". To install it use the following command: 

```
pip install -r requirements.txt
```
  
Flask application is contained in "scrape_app.py" and it is a simple web server that serves one endpoint '/scrapeIndeed'
that expects Json to be posted to it. It takes that json parses out the urls as a list and sends them off to be 
processed in the "process_url" function in "scrape.py". 

To run it, simply navigate to the directory with this repo and run "scrape_app.py" with something like:
 "python scrape_app.py" which will start the flask server and wait for json being posted to it. I used a tool called 
 Postman to post requests to "http://127.0.0.1:5000/scrapeIndeed" with payloads like:

```
Content-Type:application/json
 
{
 "urls": [
	"https://www.indeed.com/viewjob?jk=8cfd54301d909668", "https://www.indeed.com/viewjob?jk=b17c354e3cabe4f1"
	]
}
```

You can also use something like cUrl to post to the endpoint, as long as the endpoint gets a post and some legal 
json it should work.

I've also included an example Dockerfile following the same build/run path that SHOULD work on a Unix environment.
However, at time of writing I do not own any Unix environment and don't really want to duel boot on my home desktop. 
You can build it like this:

```
docker build -t indeed-scraper:latest .
```

and run it like this:

```
docker run -d -p 5000:5000 indeed-scraper:latest
```

I can get it to run on Windows but it fails due to file system differences. I can get it to work with a Windows docker
image but from what I saw from the office the people I'm submitting this to are using Mac Os and the manual or Docker
image instructions worked locally on my Mac.
