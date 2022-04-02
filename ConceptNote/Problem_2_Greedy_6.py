n = input()

dx = [2, 1, -1, -2, -2, -1,  1,  2]
dy = [1, 2,  2,  1, -1, -2, -2, -1]

x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = n[0]
y = int(n[1])
count = 0
idx = 1
for k in x_list:
    if n[0] == k:
        x = idx
    else:
        idx += 1

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        count += 1

print(count)


# 해설
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
print(column)
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, -2), (-2, 1)]
result = 0
for step in steps:
    next_row = row+step[0]
    next_colume = column+step[1]
    if next_row >= 1 and next_row <= 8 and next_colume >= 1 and next_colume <= 8:
        result += 1
print(result)

