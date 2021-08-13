N,M,K = map(int,input().split())
#N : 학생수(1-N번 학생번호)
#M: 벌칙받은 학생들의 수(M번에 걸쳐 출력됨)
#K: 벌금 내는 학생의 최저 벌칙횟수
answer=0
student = [ 0 for _ in range(N) ]
for i in range(M):
    student_num = int(input())
#idea : 크기가 N인 리스트에 벌칙횟수를 저장하고, 최저벌칙횟수를 넘기면 정답으로 출력
# 리스트를 그럼 매번 for문을 돌려서 벌칙횟수가 K를 넘는지 검사해야하나?가 관건인데
# 리스트를 업데이트할때마다 그 변수만 뽑아서 비교하면 될듯
    student[student_num-1] += 1
    if student[student_num-1] >= K :
        answer = student_num
        #answer이 다시 초기화되면 안됨, 최초의 학생이기때문
        N,M,K = map(int,input().split())
#N : 학생수(1-N번 학생번호)
#M: 벌칙받은 학생들의 수(M번에 걸쳐 출력됨)
#K: 벌금 내는 학생의 최저 벌칙횟수
answer=-1
student = [ 0 for _ in range(N) ]
for i in range(M):
    student_num = int(input())
#idea : 크기가 N인 리스트에 벌칙횟수를 저장하고, 최저벌칙횟수를 넘기면 정답으로 출력
# 리스트를 그럼 매번 for문을 돌려서 벌칙횟수가 K를 넘는지 검사해야하나?가 관건인데
# 리스트를 업데이트할때마다 그 변수만 뽑아서 비교하면 될듯
    student[student_num-1] += 1
    if student[student_num-1] >= K :
        answer = student_num
        #아마 answer이 다시 초기화 되는것때문에 통과를 못하는듯
print(answer)
#정답:최초 벌금내는 학생의 번호
print(answer)