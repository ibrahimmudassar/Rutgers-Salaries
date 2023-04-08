import concurrent.futures
import csv
from concurrent.futures import ProcessPoolExecutor

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def string_to_int(txt: str) -> int:
    intList = [str(s) for s in txt if s.isdigit()]
    return int("".join(intList))


def scrub(text):
    import string
    return ''.join(x for x in text if x in string.printable)


# open the file in the write mode
f = open('nj_salaries.csv', 'w', newline='')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(["Name", "Campus", "Department", "Title",
                "Hire Date", "Base Pay", "Gross Pay"])


def person(url: str):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    table = soup.table
    response = []

    for table_row in table.find_all("span", {"class": "cbFormData"}):
        response.append(table_row.text)

    # for table_row in table.find_all('tr')[1:]:
    #     info = [table_h.text for table_h in table_row]
    #     info.pop()
    #     info[-1] = str(string_to_int(info[-1]))

    #     response.append(info)
    #     # print(info)

    return response


def main():
    url = "https://c2eku173.caspio.com/dp/9a5950006ab05c116c684a75ae49?rnd=1680724718148&RecordID=18918&cpipage=1&PageID=8&PrevPageID=8&CPISortType=&CPIorderBy=&cbCurrentPageSize=10&cbRecordPosition="
    total = 25_553
    urls = [url + str(i) for i in range(1, total + 1)]

    with ProcessPoolExecutor() as executor:
        result = {executor.submit(person, url): url for url in urls}

        for future in tqdm(concurrent.futures.as_completed(result), total=total):

            writer.writerow(future.result())


if __name__ == '__main__':
    main()
    # close the file
    f.close()
