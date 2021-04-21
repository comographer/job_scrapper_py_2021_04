import os
from save_csv import save_to_file as save_csv
from so import get_jobs as so_jobs

# Clearing console each time program is executed
os.system("clear")

# Let user choose which job search keyword they want
search = str(input("Which job do you want? : "))

# url receives user's search input
url = f"https://stackoverflow.com/jobs?q={search}"

# hands over the complete url to so_jobs function that is in so.py
jobs = so_jobs(url)

# saves result of web scrapping in csv from function in save_csv.py
save_csv(search, jobs)
