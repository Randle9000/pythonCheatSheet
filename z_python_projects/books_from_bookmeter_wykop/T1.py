import os
for root, dirs, files in os.walk("D:/11_ksiazki/bookmeter/"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))