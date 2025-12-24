# 3일차 복습

# 변수 ~ 함수까지
# 비교하며, 설명

print("= 변수와 값 =")
# 변수와 값의 개념을 헷갈림
# 식별자 = 리터럴

age = 10
# a -> 데이터를 가리키는 이름 (변수)
# 10 ->  실제 데이터 (값)

age = 20
print(age)
# => 변수명을 값을 잘 나타낼 수 있도록 이름 짓자!


print('== 입력과 출력 ==')
print('1.입력')
# 입력 : input() 내장함수
    # 목적 : 외부로부터 값 받기(사용자가 터미널 상 입력)
    # 반환값 : 문자열(str)

# name = input('이름을 입력해주세요')
# print(name)
# print(type(name))

print('2.출력')
# 출력 : print() 내장함수
    # 목적 : 내부 값(파이썬)을 외부(터미널 상)에서 확인하기 위함
    # 반환값 : 없음

numbers = [1,2,3,4,5]    
len(numbers) # 내부에서 확인
print(len(numbers))

# 데이터 흐름
# input() : 외부(터미널) -> 내부(코드)
# print() : 내부(코드) -> 외부(터미널)

print('== 연산자 비교 ==')
print('= 산술 연산자 =')
    # 연산 대상 : 수치형
    # 반환값 : 숫자 계산 마친 값
    
a = 10 # int
b = 5.0 # float
print(a + b)

print('= 복합 연산자 =')
    # 연산 대상 : 수치형 / 가끔 문자열,리스트(+,*)
    # 반환 대상 : 산술연산 이후, 그 자리에 재할당한 값

# a = a + b
# 연산 축약
a += b
print(a)

print('= 비교 연산자 =')
    # 연산 대상 : 같은 선상에서 비교할 수 있는 것들
    # 반환 값 : True, False (bool 자료형)

# a 비교연산자 b 의 형태
    # 대소비교 : <, <=, >, >=
    # 일치비교 : ==, !=

print(a < b)

c = '오늘은'
d = '12/24'

print(c > d) # 대소 비교는 가능하나, 직관적이지 않을 수 있음
print(a != c) # 같은 자료형이 아니더라도, 일치비교는 가능

print('== 논리 연산자 ==')
    # 연산 대상 : 논리값 (True / False)
    # 반환값 : 논리값 (True/False)

# 형태 
# a and b, a or b, not a
print(True and False)

# 비교 연산과 함께 사용
print(a == b and c != d)

# 아래처럼 변수에 할당하여 사용하는 것도 가능
condition1 = a == b
condition2 = c != d

print(condition1, condition2)
print(condition1 and condition2)

# 논리연산의 단축평가
print(age)
print(age == 100 and asdlkfnqlwnecoiqhwerob)
# False and 정의되지 않은 변수
# -> 필요이상의 연산 X, 바로 거짓 반환