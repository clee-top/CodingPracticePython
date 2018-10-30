Below copied from original instructions from an email:


Project: Web Scraper

From: Jobr/Monster

Instructions:

Write a web server that scrapes job listings from Indeed and returns the job titles, locations, and company names.
The server should parallelize tasks so that it can handle a large number of URLs (up to 100 URLs) without taking too
long (less than 10s).  Please provide a timer on the server side which outputs the time taken per request.

Keep in mind that this exercise should only take a couple hours, so focus on the happy path.
Don’t spend too much time or code handling rare edge cases.

Request format:

POST /get_jobs HTTP/1.0

Content-Type: application/json

[

“http://www.indeed.com/viewjob?jk=8cfd54301d909668”,

“http://www.indeed.com/viewjob?jk=b17c354e3cabe4f1”,

“http://www.indeed.com/viewjob?jk=38123d02e67210d9”,

…

]


Response format:

HTTP/1.1 200 OK

Date: Wed, 17 May 2016 01:45:49 GMT

Content-Type: application/json

[

    {

“title”: “Software Engineer”,

“location”: “San Francisco, CA”,

“company”: “MuleSoft”,

“url”: “http://www.indeed.com/viewjob?jk=8cfd54301d909668”

},

{

“title”: “<job title>”,

“location”: “<job location>”,

“company”: “<company name>”,

“url”: “<original url>”

},

…

]

You can complete the challenge in any language you would like.
Though, please provide us with a guide on how to run the code.
Also, provide a README and a github page so that we can clone your repo and easily run the server program.
