# 탐욕 알고리즘(Greedy Algorithm)
# : 현재상황에서 좋은 것만 고르는 방법
# : 정당성 분석 - 최적의 해를 구할 수 있는지 검토 필요

# 예시 : 거스름돈 -> 최소갯수 반환
# 가장 큰 화폐단위부터 거슬러주면됨 -> 왜냐면, 화폐 단위가 큰 단위가 항상 작은 단위의 배수이므로!
n = 1260
count = 0
array = [500, 100, 50, 10]
for coin in array :
    count += n // coin
    n %= coin
print(count)

# 시간복잡도 O(k) <- 동전의 총 종류에만 영향을 받는다.

# https://hanamon.kr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%83%90%EC%9A%95%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-greedy-algorithm/
# 23분부터 다시 들어야함