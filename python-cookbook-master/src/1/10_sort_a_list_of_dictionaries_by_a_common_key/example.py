# example.py
#
# Sort a list of a dicts on a common key

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

from pprint import pprint

print("Sorted by fname:")
pprint(rows_by_fname)

print("Sorted by uid:")
pprint(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print("Sorted by lname,fname:")
pprint(rows_by_lfname)

######### lambda
rows_by_fname_lambda = sorted(rows, key= lambda r:r['fname'])
print("rows_by_fname_lambda:")
pprint(rows_by_fname_lambda)
