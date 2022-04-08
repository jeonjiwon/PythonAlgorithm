data = list(map(int, input().split()))
a = data[0]  #현재온도
b = data[1]  #목표온도
count = 0
# 현재 온도a 와 목표 온도b가 입력된다. ( 0 <= a , b <= 40 )
while True:
    if a == b:
        break
    if a < b:
        if a + 10 <= b or a+10-1 == b or a+10-2 == b:
            a += 10
            count+=1
            # print("1")
        elif a + 5 <= b or a+5-1 == b or a+5-2 == b:
            a += 5
            count+=1
            # print("2")
        else:
            a += 1
            count += 1
            # print("3")
    elif a > b:
        if  a - 10 >= b or a - 10 + 1 == b or a - 10 + 2 == b:
            a -= 10
            count += 1
            # print("4")
        elif a - 5 >= b or a - 5 + 1 == b or a - 5 + 2 == b:
            a -= 5
            count += 1
            # print("5")
        else:
            a -= 1
            count += 1
            # print("6")
print(count)