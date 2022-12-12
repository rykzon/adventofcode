#f = open("/home/rene/Documents/inventory.txt","r")
#print(f.read())
class Elve(object):
    def __init__(self,name):
        self.name = name
        self.inventory = []
    def __lt__(self,other):
        return self.suminv() < other.suminv()
    def __eq__(self,other):
        return self.suminv() == other.suminv()
    def add_inv(self,item):
        self.inventory.append(item)
    def suminv(self):
        return sum(self.inventory)

def make_elve(name):
    elve = Elve(name)
    return elve

def get_carryElve(elves):
    elves_sorted = sorted(elves,reverse=True)
    return elves_sorted[0].suminv()

def get_top3(elves):
    elves_sorted = sorted(elves,reverse=True)
    top3 = elves_sorted[0:3]
    return sum(list(map(lambda x:x.suminv(),top3)))
elves=[]
elvecounter=1
currentelve = make_elve("elve1")

with open("./0112/inventory.txt") as f:
    lines = [line.rstrip() for line in f]

for l in lines:
    if l == "":
        elvecounter=elvecounter+1
        elves.append(currentelve)
        currentelve = make_elve("elve"+str(elvecounter))
    else:
        currentelve.add_inv(int(l))
elves.append(currentelve)
print ("Top Inventory")
print (get_carryElve(elves))
print ("Top 3 Inventory")
print (get_top3(elves))