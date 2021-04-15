import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs?q=python"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
last_page = int(soup.find("a", {"class": "s-pagination--item is-selected"})["title"].replace("page 1 of ", ""))


range1 = lambda start, end: range(start, end + 1)

# def range1(start, end):
#     return range(start, end + 1)


for i in range1(1, last_page):
    print(i)
