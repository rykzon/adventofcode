responses =    {"X":    {   "points":1,
                            "beats": "C",
                            "beaten": "B",
                            "draw": "A"},
                "Y":    {   "points": 2,
                            "beats": "A",
                            "beaten": "C",
                            "draw": "B"},
                "Z":    {   "points": 3,
                            "beats": "B",
                            "beaten": "A",
                            "draw": "C"}}

prompts = {     "A":    {   
                            "beats": "Z",
                            "beaten": "Y",
                            "draw": "X"},
                "B":    {   
                            "beats": "X",
                            "beaten": "Z",
                            "draw": "Y"},
                "C":    {   
                            "beats": "Y",
                            "beaten": "X",
                            "draw": "Z"}}
def get_total (lines):
    points = 0
    for line in lines:
        if responses.get(line[2])["beats"] == line[0]:
        
            plus = 6 + int(responses.get(line[2])["points"])
      
            points = points + plus
        if responses.get(line[2])["beaten"] == line[0]:
           
            plus = int(responses.get(line[2])["points"])
         
            points = points + plus
        if responses.get(line[2])["beaten"] != line[0] and responses.get(line[2])["beats"] != line[0]:
       
            plus = 3 + int(responses.get(line[2])["points"])
       
            points = points + plus
    return points

def get_answer(lines):
    points = 0
    for line in lines:
        if line[2] == "Z":
            points = points + 6 + int(responses.get(prompts.get(line[0])["beaten"])["points"])
            #win
        if line[2] == "X":
            points = points + int(responses.get(prompts.get(line[0])["beats"])["points"])
            #lose
        if line[2] == "Y":
            points = points + 3 + int(responses.get(prompts.get(line[0])["draw"])["points"])
            #draw
    return points


with open("./0212/guide.txt") as f:
    lines = [line.rstrip() for line in f]
print(get_total(lines))
print(get_answer(lines))


