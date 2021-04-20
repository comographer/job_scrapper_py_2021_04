import os
from save_csv import save_to_file as save_csv
from so import get_jobs as so_jobs

os.system("clear")
search = str(input("Which job do you want? : "))
url = f"https://stackoverflow.com/jobs?q={search}"
jobs = so_jobs(url)
save_csv(search, jobs)
