N = int(input())
before_num = 0
count = 0
max_count = 0
for i in range(N):
    #연속하여 동일한 숫자가 나오는 횟수의 최대
    #:횟수가 크면 바로바로 초기화
    after_num = int(input())
    if before_num == 0 or after_num == before_num:
        count += 1
        if count > max_count:
            max_count = count
    else:
        max_count = count
        count = 0
    before_num = after_num
    
print(max_count)
        