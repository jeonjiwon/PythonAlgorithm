# N이 1이될때까지 반복적으로 수행
# N에서 1을 뺀다
# N을 K로 나눈다(나눠질때만 수행)

# N, K를 공백을 기준으로 구분하여 입력받기
N, K = map(int, input().split())
count = 0
while True:
    # 시간 복잡도 :  log K
    target = (N // K) * K  # N에 제일 가까운 K로 나눠지는 수
    print(N)
    print(target)
    count += (N-target)
    print(count)
    N = target
    if N < K :  # 더 이상 나눌 수 없을 때 탈출
        break
    count += 1
    # K로 나누기
    N //= K
    print('----------')
# 마지막으로 남은 수에 대해 1 씩 빼기
count += (N-1)
#     내 풀이(시간복잡도 큼..)
#     if N == 1 :
#         break
#     if N % K == 0 :
#         N = N / K
#     else :
#         N = N-1
#     count = count + 1
print('답은:', count)