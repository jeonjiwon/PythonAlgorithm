# 체육복
# 전체 학생의 수 n,
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
answer = n-len(lost)
lost.sort()
reserve.sort()
for lost_item in lost:
    # 여분을 가져온 사람이 자기 꺼를 도난 당했을 때
    if lost_item in reserve:
        answer += 1
        reserve.remove(lost_item)
        continue
    for reserve_item in reserve:
        if abs(lost_item - reserve_item) == 1 and reserve_item not in lost:
            answer += 1
            reserve.remove(reserve_item)
            break
# answer = (n-(len(lost)-answer))
print(answer)


# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     for lost_item in lost:
#         if lost_item + 1 > n or lost_item - 1 < 0:
#             continue
#         for reserve_item in reserve:
#             if lost_item + 1 == reserve_item or lost_item - 1 == reserve_item:
#                 answer += 1
#                 reserve.remove(reserve_item)
#                 break
#     return answer
# answer = solution(5,[2,4],[1,3,5])
