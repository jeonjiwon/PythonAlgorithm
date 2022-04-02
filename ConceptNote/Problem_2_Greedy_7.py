# 문자열 재정렬
# 알파벳 대문자, 숫자입력 - 알파벳을 오름차순으로 정렬하고, 뒤에 숫자들은 다 더해줌
# 예)K1KA5CB7 -> ABCKK13
data = input()
result = []
sum = 0
for i in data:
    if i.isalpha():
        result.append(i)
    else:
        sum += int(i)
result.sort()
if sum != 0:
    result.append(str(sum))
print(''.join(result))