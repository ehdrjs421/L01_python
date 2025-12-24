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