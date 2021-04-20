import requests
from bs4 import BeautifulSoup


def get_last_page(html):
    r = requests.get(html)
    soup = BeautifulSoup(r.text, "html.parser")
    if soup.find("a", {"class": "s-pagination--item is-selected"}) == None:
        return 1
    else:
        last_page = int(soup.find("a", {"class": "s-pagination--item is-selected"})["title"].replace("page 1 of ", ""))
        return last_page


def get_job(html):
    title = html.find("a")["title"]
    company = html.find("h3").find("span").text.strip()
    location = html.find("h3").find("span", {"class": "fc-black-500"}).text.strip()
    link = html.find("a")["href"]
    return {"title": title, "company": company, "location": location, "link": f"https://stackoverflow.com{link}"}


def get_jobs(html):
    last_page = get_last_page(html)
    range1 = lambda start, end: range(start, end + 1)
    jobs = []
    for page in range1(1, last_page):
        print(f"Scrapping page {page} of {last_page}...")
        r = requests.get(f"{html}&pg={page}")
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find("div", {"class": "listResults"})
        items = table.find_all("div", {"class": "fl1"})
        for item in items:
            job = get_job(item)
            jobs.append(job)
    print(f"Total {len(jobs)} jobs found")
    return jobs
