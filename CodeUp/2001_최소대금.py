# 5종류의 음식메뉴 가격
# 파 파 파 생 생
data = []
minprice1 = 2000
minprice2 = 2000
# data = list(map(int, input().split("\n")))
for i in range(5):
    a = int(input())
    data.append(a)

for i in range(len(data)):
    if i <= 2:   #파스타
        if data[i] < minprice1:
            minprice1 = data[i]
    else:  #생과일쥬스
        if data[i] < minprice2:
            minprice2 = data[i]
print(round((minprice1+minprice2) * 1.1, 2))