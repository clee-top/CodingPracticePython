from bs4 import BeautifulSoup
import requests


# Uncomment these if you use the test driver to test the code without the server.
# import json
# from multiprocessing import Pool


# This function takes one url and processes it in the manner we wish which is scraping indeed.com job listing web
# pages. It takes in a list of a url parsed from incoming requests. It returns json as described in requirements
# which are {title,location,company,url}.... as a json.


def process_url(url):
    # Test urls. Call the function with these to test.
    # mulesoft url: 'https://www.indeed.com/viewjob?jk=8cfd54301d909668'
    # healthify url: 'https://www.indeed.com/viewjob?jk=b17c354e3cabe4f1'
    # intechriti url: 'https://www.indeed.com/viewjob?jk=38123d02e67210d9'

    # Fake header so site doesn't complain as much. Sometimes they complain when you crawl without one.
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    # Requests API lets you setup retrying if you get bad responses.
    # From here: http://docs.python-requests.org/en/latest/api/
    sess = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=10)
    sess.mount('https://', adapter)

    # Blank dictionary we're going to add to from responses we scrape. Going to dump it into Json later.

    # Request URL and Beautiful soup object. Give it a timeout just in case.
    request_to_scrape = requests.get(url, headers=headers, timeout=10)

    soup = BeautifulSoup(request_to_scrape.text, "html.parser")

    # Company name reliably at this tag and class.
    company = soup.find('div', class_="icl-u-lg-mr--sm icl-u-xs-mr--xs")
    # print("The company name is: " + company.getText())

    # The title of the page has the job title and location in it.
    title_text = soup.find('title')
    title_list = str.split(title_text.text, "-")

    job_title = str.rstrip(title_list[0])
    job_location = str.rstrip(title_list[1])

    # Construct current url response into a dictionary to turn into json.
    response_dict = ({'title': job_title, 'location': job_location,
                      'company': company.getText(), 'url': url})

    # print("The current list of job dicts looks like this: " + str(response_list))

    return response_dict

# Test function so I don't have to test with the flask app and posting Json to my server.
# def test_driver():
#
#     # A simulated list of incoming json from the outside.
#    urls = ['https://www.indeed.com/viewjob?jk=8cfd54301d909668', 'https://www.indeed.com/viewjob?jk=b17c354e3cabe4f1',
#            'https://www.indeed.com/viewjob?jk=38123d02e67210d9', 'https://www.indeed.com/viewjob?jk=4e9c92bda236cabf',
#            'https://www.indeed.com/viewjob?jk=520591f85daec693', 'https://www.indeed.com/viewjob?jk=00e05d63138f195f',
#            'https://www.indeed.com/viewjob?jk=d9af9a94f5efb757', 'https://www.indeed.com/viewjob?jk=91e7ee9458e10ba1',
#            'https://www.indeed.com/viewjob?jk=d599ab7f89c83212', 'https://www.indeed.com/viewjob?jk=cb654fc18c2ec1d8']
#
#     # Build a list of the responses.
#     response_list = []
#
#     with Pool(5) as p:
#         response_list = p.map(process_url, urls)
#     # print("The response list looks like this pre-json: " + str(response_list))
#
#     # Looks a bit silly but by dumping and loading it again you get rid of the slashes and other escape characters
#     # python puts in that are valid but ugly looking json.
#     json_intermediary = json.dumps(response_list)
#     final_response = json.loads(json_intermediary)
#
#     #print(json.dumps(final_response, sort_keys=True,indent=4, separators=(',', ': ')))

# if __name__ == '__main__':
#     test_driver()
