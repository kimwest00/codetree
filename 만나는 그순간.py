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
    if d == "L":
        move = -1
    else: 
        move = 1
    for _ in range(t):
        position += move
        A.append(position)

#M개의 줄에 걸쳐, B의 이동정보 입력
position = 0
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
for i in range(len(A)):
    if A[i] == B[i]:
        print(i+1)
        break
print(A,B,len(A))
    else:
            if i == len(A)-1:
                print(-1)
#출력해야하는 답 : A,B가 최초로 만나는 시점(안만나면 -1출력)
#구현하기 어려운부분:
#    0. 번갈아 A와 B정보가 아닌, A정보 쫙, B정보 쫙
#    1.내가 계산한 방법 동시간대에 A와 B가 각각 어디있는지 위치!
#    1초) A 0 B 0
#    2초) A 1 B -1 <- 이런식으로 초(인덱스)에 따른 위치를 리스트로 만들자!