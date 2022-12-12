with open("./05/in","r") as f:
    lines = f.read()

stacks,moves = lines.split("\n\n")
moves = moves.strip().split("\n")
stacks = stacks.split("\n")
cols = []
for x in range(max(row.count("]") for row in stacks[:-1])):
    col= []
    i = x*4+1

    for y in range(len(stacks)-1):
        item = stacks[y][i]
        if item == " ":
            continue

        col.append(item)
    cols.append(col)

for move in moves:
    move = move.split()
    num = int(move[1])
    src = int(move[3])-1
    to = int(move [5])-1
    for x in range(num):
        cols[to].insert(0,(cols[src][0]))
        cols[src].pop(0)
for col in cols:
    print(col[0])




