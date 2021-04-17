import requests
from bs4 import BeautifulSoup

URL = f"https://www.indeed.com/jobs?q=python&limit=50"


def get_last_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("li")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


print(get_last_page(URL))