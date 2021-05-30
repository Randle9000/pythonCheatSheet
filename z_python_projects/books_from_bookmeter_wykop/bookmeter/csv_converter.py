import re
import csv
import pandas as pd


csv_location = 'D:/11_ksiazki/bookmeter/books.csv'


def find_sci_fi(all_genres):
    sci_list = [x for x in all_genres if re.search(r"(sf|sci.fi|scifi|sci-fi|science-fiction|science.fiction)", x)]
    print(len(sci_list))
    return sci_list


def find_fantasy(all_genres):
    fantasy_list = [x for x in all_genres if re.search(r"(fant*)", x)]
    print(len(fantasy_list))
    return fantasy_list


def find_genre(all_genres, regex):
    genre_list = [x for x in all_genres if re.search(regex, x)]
    print(len(genre_list))
    return genre_list

scifi_regex = r"(sf|sci.fi|scifi|sci-fi|science-fiction|science.fiction|s-f)"
fantasy_regex = r"(fant*)"
historical_regex = r"(hist)"
popular_science_regex = r"(popularnonaukowa)"
biography_regex = r"(biografia|wspomnienia)"
criminal_regex = r"(krymina)"
thriller_regex = r"(thriller)"
philosophy_regex = r"(filozof)"
horror_regex = r"(horror|horor)"

df = pd.read_csv(csv_location, delimiter=';')
genres_list = [genre.lower().strip() for genre in df.Gatunek_szczegolowy]
genres_set = set(genres_list)
a = find_genre(genres_set, thriller_regex)


list_of_books = []
with open(csv_location, encoding='utf8') as f:
    f_csv = csv.DictReader(f, delimiter=';')
    for row in f_csv:
        row.update({"gatunek":[]})
        book_genres = row['Gatunek_szczegolowy'].lower().strip()

        if re.search(scifi_regex, book_genres):
            row['gatunek'].append('sci-fi')
        if re.search(fantasy_regex, book_genres):
            row['gatunek'].append('fantasy')
        if re.search(popular_science_regex, book_genres):
            row['gatunek'].append('popular_science')
        if re.search(biography_regex, book_genres):
            row['gatunek'].append('biografia/wspomnienia')
        if re.search(criminal_regex, book_genres):
            row['gatunek'].append('kryminał')
        if re.search(thriller_regex, book_genres):
            row['gatunek'].append('Thriller')
        if re.search(philosophy_regex, book_genres):
            row['gatunek'].append('filozoficzna')
        if re.search(horror_regex, book_genres):
            row['gatunek'].append('horror')
        if re.search(historical_regex, book_genres):
            row['gatunek'].append('historyczna')




        if row['gatunek']:
            row['gatunek'] = '/'.join(row['gatunek'])
        else:
            row['gatunek'] = ''



        book = {'Tytuł': row['Tytuł'], 'Autor': row['Autor'], 'Gatunek_szczegolowy': row['Gatunek_szczegolowy'],
                'gatunek': row['gatunek'], 'Ocena': row['Ocena'], "Komentarz": row['Komentarz']}
        list_of_books.append(book)

if True:
    csv_name = 'D:/11_ksiazki/bookmeter/books_v2.csv'
    with open(csv_name, 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file,
                            fieldnames=list_of_books[0].keys(), delimiter=';')
        fc.writeheader()
        fc.writerows(list_of_books)