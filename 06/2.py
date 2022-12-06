with open("./06/in","r") as f:
    lines = f.read()

for i in range(13,len(lines)):
    block = lines[i-13:i+1]
    if len(set(block))==len(block):
        print(i+1)
        break

    