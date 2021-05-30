list  = [1, 2, 3, 4, 5, 6]

_, a, *b, _, _ = list # *b = 3,4, b= [3,4]
print('_: ', _)
print('a: ', a)
print('b: ', b)
print('*b: ', *b)


#####

record = ('acme', 12 ,55, 12.456, (12, 18, 2020))
name, *_, (*_, year) = record
print (name, year)

name, *_, c = record
print(name , c)