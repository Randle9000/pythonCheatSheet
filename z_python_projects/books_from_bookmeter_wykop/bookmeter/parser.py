import os, glob, re, csv
from bs4 import BeautifulSoup as bs

###############

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



def get_books(bookmeter_file, year, month):
    with open(bookmeter_file, 'r', encoding="utf-8") as file:
        bookmeter_page= file.read()

    soup = bs(bookmeter_page, 'html.parser')
    html_elements_test = soup.findAll('li', {"class": "entry iC"}, recursive=True)
    date_pattern = rf'.*{year}-{month}'
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
            list_of_books.append(
                {'Tytuł': title, "Autor": author, 'Gatunek_szczegolowy': genre, "Ocena": score, "Komentarz": comment})
            # genres.add(genre[0].split(':')[1])
            # print(title, author, genre, score)
        except IndexError:
            pass


bookmeters_files = []
a = 0
import os
for root, dirs, files in os.walk("D:/11_ksiazki/bookmeter/"):
    for file in files:
        if file.endswith(".txt"):
            root.replace("\\\\", "/")
            bookmeters_files.append(f'{root}/{file}')



list_of_books = []
for bookmeter in bookmeters_files:
    bookmeter_file = bookmeter.split('/')
    year, month = bookmeter_file[3].split('\\')
    print(bookmeter)
    get_books(bookmeter, year, month)



csv_name = 'D:/11_ksiazki/bookmeter/books.csv'
with open(csv_name, 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file,
                        fieldnames=list_of_books[0].keys(), delimiter=';')
    fc.writeheader()
    fc.writerows(list_of_books)
