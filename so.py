import requests
from bs4 import BeautifulSoup

# As there are upto 20 search result pages, I looked up last page number
def get_last_page(html):

    # using requests and BeautifulSoup module to parse html
    r = requests.get(html)
    soup = BeautifulSoup(r.text, "html.parser")

    # a class="s-pagination.." contains last page info. thus, if that is non available, search result is only one page
    if soup.find("a", {"class": "s-pagination--item is-selected"}) == None:
        return 1

    # excluding above case, last page number can be found from a class="s-pagination.." > title. cut out "page 1 of " with replace
    else:
        last_page = int(soup.find("a", {"class": "s-pagination--item is-selected"})["title"].replace("page 1 of ", ""))
        return last_page


# below function extract title, company, location, link from each job posting
def get_job(html):
    title = html.find("a")["title"]
    company = html.find("h3").find("span").text.strip()
    location = html.find("h3").find("span", {"class": "fc-black-500"}).text.strip()
    link = html.find("a")["href"]

    # combine found info from each job posting into dict
    return {"title": title, "company": company, "location": location, "link": f"https://stackoverflow.com{link}"}


def get_jobs(html):

    # get last page info from function on the top
    last_page = get_last_page(html)

    # to get range to start from 1 and end at last page, used below lambda function
    range1 = lambda start, end: range(start, end + 1)

    # create empty list that will later be appended with jobs from each page
    jobs = []

    # go to each page in range of last page
    for page in range1(1, last_page):

        # checking the progress in terminal with print function
        print(f"Scrapping page {page} of {last_page}...")

        # create URL for each page by adding "&pg={page}"
        r = requests.get(f"{html}&pg={page}")
        soup = BeautifulSoup(r.text, "html.parser")

        # this is the section that contains all job postings from each page
        table = soup.find("div", {"class": "listResults"})

        # this is all job postings on each page
        items = table.find_all("div", {"class": "fl1"})

        # for each job posting, run above get_job function
        for item in items:
            job = get_job(item)

            # add all dict to list
            jobs.append(job)
    print(f"Total {len(jobs)} jobs found")
    return jobs
