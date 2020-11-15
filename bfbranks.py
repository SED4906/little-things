import random

objects=["Teardrop","Leafy","Grassy","Blocky","Flower","Ruby","Bubble","Taco",
         "Coiny","Donut","Fanny","Barf Bag","Pin","Tennis Ball","Clock","Pen",
         "Woody","Firey","Lollipop","Gelatin","Naily","Eraser","Snowball","Gaty",
         "Black Hole","Saw","Marker","Bracelety","Pie","Bottle","David","Dora",
         "Lightning","Yellow Face","Robot Flower","Pencil","Golf Ball","Icy","Nickel","Spongey",
         "Needle","8-Ball","Remote","TV","Rocky","Roboty","Bomby","Basketball",
         "Puffball","Match","Cake","Tree","Stapy","Fries","Liy","Balloony",
         "Loser","Firey Jr.","Eggy","Bell","Cloudy","Foldy","Pillow","Book"]
ranking=[]
question = 1
for i in range(0,64):
    ranking.append([])
    for ii in range(0,64):
        ranking[i].append(0)
try:
    f = open("scores.txt")
    for i in range(0,64):
        rankstring = f.readline()
        for ii in range(0,64):
            ranking[i][ii] = int(rankstring[ii])
    question = int(f.readline())
    f.close()
except:
    pass

def writescores():
    f = open("scores.txt","w")
    for scorelist in ranking:
        for score in scorelist:
            f.write(str(score))
        f.write("\n")
    f.write(str(question))
    f.close()

for i in range(0,64):
    total = 0
    for ii in range(0,64):
        if ranking[i][ii] == 1:
            total += 1
        elif ranking[i][ii] == 2:
            total -= 1
    print(objects[i] + " " + str(total), end=" ")
print("")

c1 = 0
c2 = 0
skipped = False
while True:
    if not skipped:
        c1 = random.randint(0,63)
        c2 = random.randint(0,63)
    skipped = False
    if c1 != c2 and (ranking[c1][c2] == 0 or ranking[c2][c1] == 0):
        print("Question " + str(question) + ": " + objects[c1] + " or " + objects[c2] + " (1/2/S/Q)")
        choice = input()
        if choice == "1":
            ranking[c1][c2] = 1
            ranking[c2][c1] = 2
            question += 1
        elif choice == "2":
            ranking[c1][c2] = 2
            ranking[c2][c1] = 1
            question += 1
        elif choice == "S":
            writescores()
            skipped = True
        elif choice == "Q":
            break
        else:
            skipped = True
    else:
        skipped = False
