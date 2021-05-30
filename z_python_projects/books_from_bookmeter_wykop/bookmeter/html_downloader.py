import requests
import re
import os
from bs4 import BeautifulSoup as bs
from pathlib import Path


def download_all_pages(year=2020, month=10, url='', pages=None):
    if pages is None:
        pages = []

    base_url = url
    next_pages_pattern = r'https://www.wykop.pl/tag/bookmeter/archiwum/{0}-{1}/nex.*/?'.format(year, month)
    previous_month = int(month) - 1

    if previous_month is 0:
        previous_year = int(year) - 1
        december = 12
        date_pattern = rf'.*{previous_year}-{december}'
    elif previous_month > 9:
        date_pattern = rf'.*{year}-{previous_month}'
    else:
        date_pattern = rf'.*{year}-0{previous_month}'

    response = requests.get(base_url)
    soup = bs(response.text, 'html.parser')
    list_of_next_pages = soup.find_all('a', {'href': re.compile(next_pages_pattern)})

    if len(list_of_next_pages) == 1:
        next_page_url = soup.find_all('a', {'href': re.compile(next_pages_pattern)})[0]['href']
    else:
        next_page_url = soup.find_all('a', {'href': re.compile(next_pages_pattern)})[1]['href']

    date = soup.find_all('time', {'title': re.compile(date_pattern)})

    print(date_pattern)
    if date:
        pages.append(next_page_url)
        return {f'{month}-{year}': pages}
    else:
        pages.append(next_page_url)
        return download_all_pages(year, month, next_page_url, pages)


url_1 = 'https://www.wykop.pl/tag/bookmeter/'
url_template = 'https://www.wykop.pl/tag/bookmeter/archiwum/{0}-{1}/'


def get_pages_per_month(years=None, months=None):
    if years is None:
        years = ['2016', '2017', '2018', '2019', '2020'] #
    if months is None:
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    date_boookmeter_pages = {}
    for year in years:
        for month in months:

            if year is '2020' and month is '10':
                break

            base_url = url_template.format(year, month)
            date_pages = download_all_pages(year, month, url=base_url, pages=[base_url])
            date_boookmeter_pages.update(date_pages)
    return date_boookmeter_pages


def download_pages_as_html(dict_of_pages, path="D:/11_ksiazki/bookmeter"):
    book_path = Path(path)
    for date, pages in dict_of_pages.items():
        month, year = date.split('-')
        book_folder = book_path / year/ month
        itr = 1

        if not os.path.exists(book_folder):
            os.makedirs(book_folder)

        for page in pages:
            local_path = book_folder / f'{year}-{month}_bookmeter_{itr}.txt'
            r = requests.get(page)
            with open(local_path, 'w', encoding="utf-8") as file:
                file.write(r.text)
            itr += 1

date_pages = get_pages_per_month()
download_pages_as_html(date_pages)
