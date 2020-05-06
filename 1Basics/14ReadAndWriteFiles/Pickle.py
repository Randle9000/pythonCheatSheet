#Python offers for this purpose a module, which is called "pickle". With the algorithms of the pickle module we can serialize and de-serialize Python object structures.
import pickle

cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
fh = open("data.pkl", "bw")
pickle.dump(cities, fh)
fh.close()

f = open("data.pkl", "rb")
villes = pickle.load(f)
print(villes)