import requests
import re
import csv
from bs4 import BeautifulSoup as bs

url_1 = 'https://www.wykop.pl/tag/bookmeter/'
url_template = 'https://www.wykop.pl/tag/bookmeter/archiwum/{0}-{1}/'


def get_pages_for_month_and_year(year=2020, month=10, url='', pages = []):
    pages = pages
    date = 1
    base_url = url
    next_pages_pattern = r'https://www.wykop.pl/tag/bookmeter/archiwum/{0}-{1}/nex.*/?'.format(year, month)
    month_1 = int(month) - 1

    if month_1 is 0:
        year_1 = int(year) - 1
        month_2 = 12
        date_pattern = rf'.*{year_1}-{month_2}'
    elif month_1 > 9:
        date_pattern = rf'.*{year}-{month_1}'
    else:
        date_pattern = rf'.*{year}-0{month_1}'

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
        return pages
    else:
        pages.append(next_page_url)
        return get_pages_for_month_and_year(year, month, next_page_url, pages)


pattern_title = r'Tytu.*'
pattern_author = r'Autor.*'
pattern_genre = r'Gatunek.*'
pattern_score = [r'.*★.*', r'Ocena.{1,2}\d?']
genres = set()


def find_genre(text):
    genre = re.compile(pattern_genre).findall(text)
    if not genre:
        return "not defined"
    return genre


def find_score(text):
    score = re.compile(pattern_score[0]).findall(text)
    if score:
        return score[0].count('★')
    else:
        score = re.compile(pattern_score[1]).findall(text)
        score = re.compile('\d').findall(score[0])[0]
        return score


def find_description(text):
    score_index = ''
    hash_index = ''
    text_splitted = text.split('\n')
    text_splitted = [x for x in text_splitted if x]
    for i,x in enumerate(text_splitted):
        if re.search(r'.*★.*', x):
            score_index = i
            break
        elif re.search(r'Ocena.{1,2}\d?', x):
            score_index = i
            break

    for i, x in enumerate(text_splitted):
        if re.search(r'.*#.*', x):
            hash_index = i

    comment = '\n'.join(text_splitted[score_index+1 : hash_index])
    return comment


list_of_books = []
for year in ['2015', '2016', '2017', '2018', '2019', '2020']:
    for month in ['01', '02' ,'03', '04','05','06','07','08','09','10','11','12']:
        base_url = url_template.format(year, month)
        list_of_pages = get_pages_for_month_and_year(year, month, url=base_url, pages=[base_url])

        if year is '2020' and month is '10':
            break

        for url in list_of_pages:
            print(url)
            response = requests.get(url)
            soup = bs(response.text, 'html.parser')
            html_elements = soup.findAll("div", {"class": "text"})
            html_elements_test = soup.findAll('li', {"class": "entry iC"}, recursive=True)
            date_pattern = rf'.*{year}-{month}'
            current_year_month = year + '-' + month
            for html_element in html_elements_test:
                time = html_element.findAll('time', {'title': re.compile(date_pattern)})
                if not time:
                    continue

                book_div = html_element.findAll("div", {"class": "text"})[0]
                text = book_div.text
                try:
                    title = re.compile(pattern_title).findall(text)
                    if not title:
                        continue
                    title = title[0].split(':')[1].replace(';', ' ')
                    author = re.compile(pattern_author).findall(text)[0].split(':')[1].replace(';', ' ')
                    genre = find_genre(text)[0].split(':')[1].replace(';', ' ')
                    score = find_score(text)
                    comment = find_description(text).replace(';', ' ')
                    list_of_books.append({'Tytuł':title, "Autor":author, 'Gatunek':genre, "Ocena":score, "Komentarz":comment})
                    #genres.add(genre[0].split(':')[1])
                    #print(title, author, genre, score)
                except IndexError:
                    print(title, 'error')


csv_name = 'books.csv'
with open(csv_name, 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file,
                        fieldnames=list_of_books[0].keys(), delimiter=';')
    fc.writeheader()
    fc.writerows(list_of_books)




