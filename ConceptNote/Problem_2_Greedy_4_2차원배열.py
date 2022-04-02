n = int(input())
data = list(map(str, input().split()))

#    R   U   L   D
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 1, 1

move_types = ['R', 'U', 'L', 'D']
for d in data:
    for i in range(len(move_types)):
        if d == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # if d == 'R':
    #     ny = y + dy[0]
    # if d == 'L':
    #     ny = y + dy[2]
    # if d == 'U':
    #     nx = x + dx[1]
    # if d == 'D':
    #     nx = x + dx[3]

    # 공간을 벗어나는 경우 건너뛰기
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)




