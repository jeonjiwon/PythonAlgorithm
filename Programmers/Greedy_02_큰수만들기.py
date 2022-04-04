# 큰수만들기
print("number 입력 >")
number = list(map(str, input()))
print("k 입력 >")
k = int(input())  # 제거해야할 길이
answer = []
# 스택
# 탐욕법 : 예) number = 1924, k=2 일때
#            10의 자리는 10의 자리가 될 수 있는 192 중에서의 max값
#             1의 자리는 1의 자리가 될 수있는 24 중에서 max값
for num in number:
    # 큐에 있는 숫자 < 리스트에 있는 숫자 이면 큐에 있는 숫자를 제거하고 k를 줄여준다.
    # stack[-1] : stack의 top 찾을때 (제일 최근...제일 위!)
    while answer and k > 0 and answer[-1] < num:
        answer.pop()
        k -= 1
    # 최초 실행 시에는 무조건 큐에 넣어준다.
    # 큐에 있는 수보다 리스트에 있는 수가 적으면 넣어준다.
    answer.append(num)
answer = ''.join(answer[:len(number) - k])
print(answer)

# 해설 =>
# https://train-validation-test.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level-2-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
