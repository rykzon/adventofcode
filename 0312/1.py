with open("./0312/in") as f:
    lines = [line.rstrip() for line in f]

values = (list(map(chr, range(97, 123)))) + (list(map(chr, range(65, 91))))


priosum = 0
for ruck in lines:
    done = ""
    comp1,comp2 = ruck[:len(ruck)//2],ruck[len(ruck)//2:]
    for c in comp1:
        if comp2.find(c) > -1 and done.find(c) == -1:
            priosum=priosum+values.index(c)+1
            done = done + c
print(priosum)
           