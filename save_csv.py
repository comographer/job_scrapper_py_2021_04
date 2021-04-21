import csv


def save_to_file(search, jobs):
    # creating empty csv file with {search} as name and in write-only mode
    file = open(f"{search.lower()}.csv", mode="w")

    # writer function let's you to write in the argument file
    writer = csv.writer(file)

    # adding first row with writerow
    writer.writerow(["title", "company", "location", "link"])

    # adding each row to the csv file
    for job in jobs:
        writer.writerow(list(job.values()))
    return