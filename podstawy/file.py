path="/home/grzegorz/file"

plik=open(path, "r")

print(plik.read())

for line in plik:
    print(line)