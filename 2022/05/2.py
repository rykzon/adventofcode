from collections import deque
with open("./05/in","r") as f:
    lines = f.read()

stacks,moves = lines.split("\n\n")
moves = moves.strip().split("\n")
stacks = stacks.split("\n")
cols = deque()
for x in range(max(row.count("]") for row in stacks[:-1])):
    col= deque()
    i = x*4+1
    for y in range(len(stacks)-1):
        item = stacks[y][i]
        if item == " ":
            continue
        col.append(item)
    cols.append(col)

for move in moves:
    add=[]
    move = move.split()
    num = int(move[1])
    src = int(move[3])
    to = int(move [5])
    for _ in range(num):
        add.append(cols[src - 1].popleft())

    for i in reversed(add):
        cols[to - 1].appendleft(i)

for col in cols:
    print(col[0])




