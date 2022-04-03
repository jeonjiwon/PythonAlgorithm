# 체육복
# 전체 학생의 수 n,
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
answer = len(reserve)
# lost.sort()
# reserve.sort()

for lost_item in list:
    for reserve_item in reserve:
        if lost_item + 1 == reserve_item or lost_item - 1 == reserve_item:
            answer += 1

print(answer)




