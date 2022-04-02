# 정수 n 입력
# 00시 00분 00초부터 n시 59분 59초 까지 3이 하나라도 포함되는 수 출력
# 5 입력시 11475 출력
# 완전탐색(brute forcing) 문제 유형 : 가능한 모든 수를 다 탐색
# 24 * 60 * 60 => 최대 86,400가지
h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)

