# 메서드 

# 딕셔너리
    # 순서 : X
    # 변경 : O
    # 중복 : X (key 값)

students = {'jun':40,
            'alex':20,
            'kyle':30,
            'ken':22}
print(students)

# 값 조회
print(students['jun'])
# print(students['chelsea']) # KeyError: 'chelsea'

# 값 조회 : get 메서드
# key를 기준으로 value를 반환합니다. 
# 만약 값이 없으면,반환할 값이 없다는 None을 나타냅니다.

print(students.get('ken'))
print(students.get('chelsea')) # 없는 경우, 에러를 발생 시키지 않음
print(students.get('chelsea','key가 존재하지 않습니다.'))


# 수정
students.update({'jun':300})
print(students)

# 추가
students.update({'chelsea':30})
print(students)

# 삭제
# 전달된 키에 해당하는 한 쌍을 삭제
# 실제 삭제되는 값을 보지 못하므로, 삭제되는 값을 반환
deleted_student = students.pop('alex')
print(deleted_student)
print(students)

deleted_student = students.pop('heather','학생이 없습니다.')
print(deleted_student)

# 집합 (set)
    # 순서 : X
    # 수정 : O
    # 중복 : X

numbers_1 = {1,3,5,7,9}
numbers_2 = {1,2,3,4,5}

# 집합 연산
print(numbers_1.intersection(numbers_2)) # 교집합
print(numbers_1.difference(numbers_2)) # 차집합
print(numbers_1.union(numbers_2)) # 합집합
# 바꿔도 되는지 잘 모름

# 추가 : add()
numbers_1.add(10000)
print(numbers_1)

numbers_1.add(1)
numbers_1.add(1)
numbers_1.add(1)
numbers_1.add(1)
numbers_1.add(1)

print(numbers_1) # 중복을 허락하지 않음

# 여러 값 추가 : update()
# 
numbers_1.update([99,999,9999])
print(numbers_1)

# 삭제 : remove() / discard()
numbers_1.remove(10000)
print(numbers_1)

# numbers_1.remove(10000) # KeyError: 10000
# print(numbers_1)

numbers_1.discard(1)
print(numbers_1)

numbers_1.discard(1)
print(numbers_1)