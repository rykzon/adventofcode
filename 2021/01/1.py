with open("./2021/01/in","r") as f:
    lines = [line.strip() for line in f]
count = 0
for i in range(1,len(lines)):
    if int(lines[i])>int(lines[i-1]):
        count+=1
print(count)

    