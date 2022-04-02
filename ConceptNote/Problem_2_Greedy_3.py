# 모험가 n명
# 공포도가 x인 모험가는 반드시 x명 이상 그룹에 참여해야함
# 최대 만들 수 있는 모험가 그룹
# 모든 모험가를 특정한 그룹에 넣을 필요는 없음

# 5
# 2 3 1 2 2
n = int(input())   # 모험가 수
data = list(map(int, input().split()))  # 모험가 공포도 정보
data.sort()   # 공포도가 낮은 것부터 정렬
print(data)

result = 0  # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i :   # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1
        count = 0
print(result)



