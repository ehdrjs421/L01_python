# 내장 함수
# 파이썬 자체적으로 제공하는 함수

# len() 
# 컨테이너 자료형의 item 갯수를 세어 반환
# 길이를 반환한다.
numbers = [1,2,3,4,5]
print(len(numbers))

word = 'Hello python!'
print(len(word))

# is_male = True
# print(len(is_male)) # 에러 발생

# 사용자 정의함수 len_func 작성
numbers = [2, 45, 6, 8, 2543, 8, 32, 6, 2, 6, 8]

# 1단계 : 정의
# 내장함수 len 을 구현해 보기
def len_func(container):
    answer = 0 # 값을 세어내기 위한 초기값 설정
    for _ in container:
        answer += 1
    return answer

# 2단계 : 호출
print(len_func(numbers))

# 내장함수 sum()
print(sum(numbers))

def sum_func(container):
    answer = 0
    for item in container:
        answer += item
    return answer

print(sum_func(numbers))

# 최댓값
print(max(numbers))

# 최솟값
print(min(numbers))

# sorted() 내장함수
# 입력받은 컨테이너 자료형을 정렬하여, 새로운 리스트를 반환
# 오름차순(기본), 정렬의 기준도 바꿀 수 있음!

numbers = [2, 5, 1, 7, 8] # 리스트 = 순서 O
# 순서가 존재한다는 것은 정렬된 것이 아니다.

numbers_new = sorted(numbers)
print(numbers_new)
print(id(numbers_new))

print(numbers)
print(id(numbers))

print(sorted(numbers,reverse=True))
print(sorted(numbers, key=lambda x:-x)) # 익명함수를 넣어서 조절도 가능

users = {
        'name':['jun','alex','chelsea'],
        'age':[21,19,22],
        'is_male':[True,True,False]
        }

print(sorted(users))

# 내장함수 map()
# 컨테이너 자료형의 각원소에 함수를 적용한 후, 그 결과를 반환

number_str = '12345'
print(int(number_str))

# 아래 코드를 내장함수 map을 통해 한번에 줄임
# 방법 1
numbers = []
for n in number_str:
    numbers.append(int(n))
print(numbers)

# 방법 2
numbers = list(map(int,number_str))
print(numbers)
# -> 대안이 있다면, 더 편한 방식 선택