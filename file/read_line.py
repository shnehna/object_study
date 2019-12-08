file = open("readme.txt", encoding="utf-8")
while True:
    readline = file.readline()
    if not readline:
        break
    print(readline)
file.close()
