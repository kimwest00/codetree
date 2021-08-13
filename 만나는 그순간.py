N,M = map(int,input().split())
#N개의 줄에 걸쳐, A의 이동정보 입력
    #(방향(L,R), 시간(t)
    #L <- 반대방향으로 이동
A=[]
B=[]
position = 0
total_time = 0
for i in range(N):
    d,t = input().split()
    t = int(t)
    total_time += t
    if d == "L":
        move = -1
    else: 
        move = 1
    for _ in range(t):
        position += move
        A.append(position)

#M개의 줄에 걸쳐, B의 이동정보 입력

for i in range(M):
    d,t = input().split()
    t = int(t)
    if d == "L":
        move = -1
    else: 
        move = 1
    for _ in range(t):
        position += move
        B.append(position)
for i in range(total_time):
    if A[i] == B[i]:
        print(i)
        break