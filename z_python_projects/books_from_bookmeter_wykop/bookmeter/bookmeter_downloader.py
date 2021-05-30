import requests
import re
import os
import csv
from bs4 import BeautifulSoup as bs
from pathlib import Path

# url_template = 'https://www.wykop.pl/tag/bookmeter/archiwum/{0}-{1}/'

################
################
################

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





