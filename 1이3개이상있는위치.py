n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#인접한다 = [a][b] 에서 [a-1][b] [a][b-1] [a+1][b] [a][b+1]
cell_count = 0
count = 0
#무식하게 하나하나 다 세볼거다
for i in range(n):
    for j in range(n):
        try:
            if arr[i-1][j]==1 and i-1>=0:
                count +=1
            if arr[i][j-1]==1 and j-1>=0:
                count +=1
            if arr[i+1][j] ==1 and i+1 <=n:
                count +=1
            if arr[i][j+1] == 1 and j+1 <=n:
                count +=1
        except:
            pass
        if count >= 3:
            cell_count +=1
        count = 0