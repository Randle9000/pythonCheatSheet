fobj = open("ad_lesbiam.txt", "r") # r read from file
fobj.close()

fobj = open("ad_lesbiam.txt")
for line in fobj:
    print(line)
for line in fobj:
    print(line.rstrip())
fobj.close()

###################
#Writting
print()

fh = open("example.txt", "w") # write mode with 'a' is an append mode
fh.write("To write or not to write\nthat is the question!\n")
fh.close()

#same as above but automatically closed
with open("example.txt", "w") as fh:
    fh.write("To write or not to write\nthat is the question!\n")

poem = open("ad_lesbiam.txt").readlines() # read all lines in one file

poem = open("ad_lesbiam.txt").read()
print(poem[16:34])

fh = open('colours.txt', 'w+')
fh.write('The colour brown')

# Go to the 12th byte in the file, counting starts with 0
fh.seek(11)
print(fh.read(5))
print(fh.tell())
fh.seek(11)
fh.write('green')
fh.seek(0)
content = fh.read()
print(content)