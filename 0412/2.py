with open("./0412/in") as f:
    lines = [line.rstrip() for line in f]
counter = 0
for pair in lines:
    if (int(pair.split(",")[0].split("-")[0]) <= int(pair.split(",")[1].split("-")[1]) and int(pair.split(",")[1].split("-")[0]) <= int(pair.split(",")[0].split("-")[1])):
        counter = counter +1
print(counter)