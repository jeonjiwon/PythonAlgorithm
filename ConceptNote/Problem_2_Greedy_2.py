# 만들어질수 있는 가장 큰 수 출력
# s = input()  # 0 ~ 9 까지 수, +, * 사용

array = [1, 2, 9, 8, 4]
maxvalue = 0
for a in array:
    # print(a)
    if a <= 1 or maxvalue <= 1:
        maxvalue += a
    else:
        maxvalue *= a
print(maxvalue)

#해설
data = input()
result = int(data[0])
for i in range(1, len(data)) :
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else :
        result *= num
print(result)