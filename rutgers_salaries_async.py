import concurrent.futures

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def string_to_int(txt: str) -> int:
    intList = [str(s) for s in txt if s.isdigit()]
    return int("".join(intList))


def scrub(text):
    import string
    return ''.join(x for x in text if x in string.printable)


def person(url: str):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.table
    response = []

    for table_row in table.find_all("span", {"class": "cbFormData"}):
        response.append(table_row.text)

    return response


url = "https://c2eku173.caspio.com/dp/9a5950006ab05c116c684a75ae49?rnd=1680724718148&RecordID=18918&cpipage=1&PageID=8&PrevPageID=8&CPISortType=&CPIorderBy=&cbCurrentPageSize=10&cbRecordPosition="
total = 25_553
urls = [url + str(i) for i in range(1, total + 1)]

persons = []

with concurrent.futures.ThreadPoolExecutor() as executor:

    # Submit the tasks to the executor
    results = [executor.submit(person, url)
               for url in urls]

    # Get the results as they complete
    for future in tqdm(concurrent.futures.as_completed(results), total=len(results)):
        persons.append(future.result())

df = pd.DataFrame(persons, columns=["Name", "Campus", "Department", "Title",
                                    "Hire Date", "Base Pay", "Gross Pay"])

df.to_csv("rutgers_salaries.csv")
