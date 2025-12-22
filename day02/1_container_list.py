# 컨테이너 자료형
print('=== 리스트 (list) ===')
# 연속되어 있는, 순서가 존재하는, 가변 자료형
# 0개 이상의 값을 순서 있게 저장하는 자료형

# 대괄호 []를 통해 생성
numbers = [10,20,30,40,50]
print(numbers)
print(type(numbers))

example = [10, "20", 30.0, 40, 50, True, False, []]
print(example)
print(type(example))

# 비어있는 리스트도 리스트다.
empty = []
print(empty)
print(type(empty))
print(bool(empty)) # False

# 리스트 연산
# + 연산 : 리스트끼리 연결
# 리스트 + 리스트
number_1 = [1, 2]
number_2 = [3, 4]
number_3 = number_1 + number_2 # 연결하여, 신규 리스트 생성

print(number_3)

print(id(number_1))
print(id(number_2))
print(id(number_3))

# => 연산의 결과, 새로운 리스트를 생성

# * 연산 : 같은 리스트를 n번 반복하여 합쳐서 "새로운 리스트" 생성
# 리스트 * 반복 횟수(int)
print(number_1)
# print(number_1 * number_2) # 에러 발생
# print(number_1 * 1.5) # 에러 발생
print(number_1 * 3)

print(id(number_1))
print(id(number_1 * 3))


print("==== 리스트의 특징 ====")
print('== 특징 1. 순서가 있는 자료형 ==')

print('= 인덱싱 =')
# 인덱싱(indexing) = 인덱스(index)라고 하는 위치를 기준으로 원소에 접근
# 리스트[인덱스] -> 인덱스 위치의 원소를 확인

# 인덱스 0 부터 시작
numbers = [10, 20, 30, 40, 50]
# 인덱스      0, 1,   2,  3,  4    (0부터 시작하여, n-1번까지 존재)
# 음수 인덱싱 -5, -4, -3, -2, -1    (-1가 가장 마지막 원소)

print(numbers[0])
print(numbers[1])
# ...
print(numbers[4])
# print(numbers[5]) # IndexError 발생

print(numbers[-1])

print('== 슬라이싱 ==')
# 리스트[시작:끝:간격]
# 이때, 시작/끝/간격을 나타내는 숫자
print(numbers[1:4])
print(numbers[5:2:-1])

# 리스트 뒤집기
print(numbers[::-1]) # 리스트를 뒤집는 pythonic 한 방법

# 리스트의 특징 2: 가변 자료형 
# "가"능하다, "변"경이 -> 수정, 삭제, 추가 가능
# 객체 자체를 바꾸지 않고도 변경 가능

print('= 변경 가능 =')
# 1. 수정
print(numbers)
print(id(numbers))
numbers[1] = -1

print(numbers)
print(id(numbers)) 
# 값을 수정하더라도 객체의 주소값이 바뀌지 않는다.

# 2. 추가
# 리스트의 가장 마지막 위치에 추가 

# numbers[5] = 60 # 에러발생
numbers.append(60)
print(numbers)

print(id(numbers))

# 3. 삭제
numbers.pop() # 가장 마지막 요소 삭제
print(numbers)
print(id(numbers))

# 자료형 자체를 변경하더라도, 주소값에 영향이 없다.