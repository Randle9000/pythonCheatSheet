import pandas as pd

def splitter(additional_information=''):
    print('\n\n####### {0} #########\n'.format(additional_information))

first = ('Mike', 'Tom', 'Bill', 'Mat')
last = ('Kowalsky', 'Morillo', 'Rurke', 'K')
job = ('data analyst', 'Manager', 'doctor', 'physycist')
lang = ('pythpn', 'java', 'Brain', 'python')

df = pd.DataFrame(list(zip(last, job, lang)), columns=['last', 'job', 'lang'], index=first)
print(df)

# accessing Bill
splitter('accessing Bill')
print("""df.loc['Bill', 'job']: """, '\n', df.loc['Bill', 'job'], '\n')
df.loc['Bill', 'job'] = "data enginner"
print("""df.loc['Bill', 'job'] = "data enginner:""", '\n',  df.loc['Bill'], '\n')
df.at['Tom', 'lang'] = 'C++'
print("""df.at['Tom', 'lang'] = 'C++'""", '\n', df.loc['Tom', 'lang'])

#replace
splitter('replace')
df.replace('Kowalsky', 'Novak', inplace=True) # Kowalsky can be the list it does not have be value, it can be a list with regexes!
print("""df.replace('Kowalsky', 'Novak', inplace=True)""", '\n', df)


