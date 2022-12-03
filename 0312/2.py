with open("./0312/in") as f:
    lines = [line.rstrip() for line in f]

values = (list(map(chr, range(97, 123)))) + (list(map(chr, range(65, 91))))

priosum = 0

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

groups = (list(chunks(lines,3)))
for group in groups:
    done = ""
    for c in group[0]:
        if group[1].find(c) > -1 and group[2].find(c) > -1 and done.find(c) == -1:
            print(c)
            done = done + c
            priosum=priosum+values.index(c)+1

print(priosum)