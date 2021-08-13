move = input()
N = len(move)
xdir = 0
ydir= 1
xposition = 0
yposition = 0
for i in move:
    if i =="L":
        #반시계방향
        #(0,1)->(-1,0)->(0,-1)->(1,0)->(0,1)
        empty = xdir
        xdir = -ydir
        ydir = empty
    elif i=="R":
       #시계방향
        #(0,1)->(1,0)->(0,-1)->(-1,0)->(0,1)
        empty = xdir
        xdir = ydir
        ydir = -empty
    else:#i==F
        xposition += xdir
        yposition += ydir
print(xposition,yposition)