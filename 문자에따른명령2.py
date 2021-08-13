move = input()
N = len(move)
xdir = 0
ydir= 1
xposition = 0
yposition = 0
for i in move:
    if i =="L":
        xdir = -1
        ydir = 0
    elif i=="R":
        xdir = 1
        ydir = 0
    else:#i==F
        xposition += xdir
        yposition += ydir
print(xposition,yposition)