# 컨테이너 자료형
# 딕셔너리
# key:value의 한쌍으로 이루어져 있다.
user = {'name':'jun',
        'age':30, 
        'license':True, 
        'city':'seoul',
        'age':30.5}
        # []:'선언 불가'} # TypeError: unhashable type: 'list'
        # {'k':'v'}:'선언 불가'} # TypeError: unhashable type: 'dict'
    
# key 는 바뀔수 없는 자료형이여야만 한다.
# key 는 유일하다. --> 중복 불가

print(user)
print(type(user))
print(len(user))

# 특징 1: 순서가 없는 컨테이너
print(user['name']) # 위치로 인덱싱하여 값을 살펴보는 것이 아님
print(user['age'])  # key를 기준으로 value에 접근한다.
# print(user[0]) # 위치로 불러올 수 없음 -> KeyError: 0

# 특징 2: 가변 자료형 (mutable)
# 변경 -> 수정, 추가, 삭제
# 값을 변경하여도 똑같은 주소 (id)를 가진다.

# 수정
print(id(user))

user['age'] = 32 # 할당 가능
print(user)
print(id(user))

# 추가
# 할당 가능!
user['nationality'] = 'korea'
print(user)

# 삭제
user.pop('city')
print(user)

# optional
# 딕셔너리 메서드 간단 설명
# 딕셔너리의 key 살펴보기
print(user.keys())
print(type(user.keys()))
print(list(user.keys()))

# 딕셔너리 value 살펴보기
print(user.values())
print(type(user.values()))
print(list(user.values()))

# key:value 한 쌍으로 보기
# key:value의 역할을 무시하고, (쌍을 제거) 튜플로 반환
print(user.items())

for k in user.keys():
    if k == 'nationality' or k == 'city':
        print(f'{user[k]} 출신')

for k, v in user.items():
    print(f'{k}는 {v}입니다.')