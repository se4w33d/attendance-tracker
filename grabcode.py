import requests
from urllib.parse import urlparse, parse_qsl
from bs4 import BeautifulSoup

def get_attendance_code(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    res = soup.find_all('script')[-1]
    if res:
        sc_content = res.string

    target_url = sc_content.split("url: \"")[-1].split("&sortBy=\"")[0]

    parsed_url = urlparse(target_url)
    parsed_query = parse_qsl(parsed_url[4]) # index 4 is the query
    
    return (parsed_query[0][1], parsed_query[1][1])
