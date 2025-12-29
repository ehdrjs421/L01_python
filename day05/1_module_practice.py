# 카운트다운이 있는 로또 번호 추첨기 만들기

# 1. 5초 카운트다운 
# 2. 1 ~ 45 수 중, 6개 숫자 무작위 출력
# 3. 5개의 숫자는 오름차순 정렬 필요

import random
import time

# 반복문으로 남은 초 세기
# 방법 1 : range 를 이용한 카운트 다운
for i in range(5, 0, -1):
    print(f'{i}초 남았습니다.')
    time.sleep(1)
    
# 방법 2 : f-string 표현식 수정
# for i in range(5):
#     print(f'{5-i}초 남았습니다.')
#     time.sleep(1)

# 랜덤 번호 추출
numbers = range(1, 46) # 연속된 정수 목록
lotto = list(random.sample(numbers, 6))

# 정렬
lotto.sort()
print(lotto)