import os
from so import get_jobs as so_jobs

os.system("clear")
search = str(input("Which job do you want? : "))
url = f"https://stackoverflow.com/jobs?q={search}"
so_jobs(url)