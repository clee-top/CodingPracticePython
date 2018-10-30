from flask import Flask, request
from multiprocessing import Pool
import json
import time
from scrape import process_url

# Requirements example of input wasn't legal json, so I just went ahead and made as simple and as close to requirements
# as possible. Here's an example of the input to this webserver adapted from the requirements example to be legal json.
# {
#     "urls": [
#         "https://www.indeed.com/viewjob?jk=8cfd54301d909668",
#         "https://www.indeed.com/viewjob?jk=b17c354e3cabe4f1",
#         "https://www.indeed.com/viewjob?jk=38123d02e67210d9"
#     ]
# }

app = Flask(__name__)


# This Flask webserver serves one endpoint "/scrapeIndeed". If you post something like the above example it will spool
# up some subprocesses to process the urls and scrape their content. Currently configured at 20 since the requirements
# said they wanted to process up to 100 url's in less then 10 seconds and 20 subprocesses is a fairly sane amount for
# most common machines this server would run on. It also chugs through 100 urls in ~ 3 seconds on my machine with
# these settings.

@app.route('/scrapeIndeed', methods=['POST'])
def scrape_indeed():

    if not request.is_json:
        print("Incoming request not legally formatted Json, please try with legal Json.")
        return 'Bad_Request'

    # Flask request.get_json to turn incoming json into a dictionary.
    incoming_json = request.get_json()
    # print("Incoming url's look like these: " + str(incoming_json['urls']))

    # Build a list of the responses when processing urls.
    response_list = []

    # Keep time for all the responses
    start_processing_time = time.time()

    # This spawns up to five sub-processes to churn through the incoming urls.
    with Pool(20) as p:
        response_list = p.map(process_url, incoming_json['urls'])
    # print("The response list looks like this pre-json: " + str(response_list))

    # Calculate processing time for all the requests.
    end_processing_time = time.time()
    total_time = end_processing_time - start_processing_time

    print("The scraping server processed: " + str(len(incoming_json['urls'])) + " requests in a total time of: "
          + str(total_time) + " taking an average of " + str(total_time / len(incoming_json['urls'])) +
          " seconds per request.")

    # Looks a bit silly but by dumping and loading it again you get rid of the slashes and other escape characters
    # python puts in that are valid but ugly looking json.
    json_intermediary = json.dumps(response_list)
    final_response = json.loads(json_intermediary)

    # Print out the responses nicely for people.
    print(json.dumps(final_response, sort_keys=True,indent=4, separators=(',', ': ')))

    return 'HTTP 200 Success'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)