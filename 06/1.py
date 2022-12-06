with open("./06/in","r") as f:
    lines = f.read()

for i in range(3,len(lines)):
    block = lines[i-3:i+1]
    if len(set(block))==len(block):
        print(i+1)
        break

    