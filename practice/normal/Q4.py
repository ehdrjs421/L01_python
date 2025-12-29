# [실습 4] 
# 과목별 점수가 담긴 리스트(scores)를 입력받아 합격 여부를 판정하는 함수를 만드시오.

# [합격 조건]
# 1. 모든 과목의 평균 점수가 60점 이상이어야 합니다.
# 2. 단, 한 과목이라도 40점 미만(과락)이 있으면 평균과 관계없이 'FAIL'입니다.

# [반환값]
# 합격일 경우 "PASS", 불합격일 경우 "FAIL"을 반환

def check_result(scores):
    # pass를 지우고 로직을 작성합니다.
    pass

# 테스트 코드
print(f"결과 1 (PASS 예상): {check_result([80, 90, 75])}")
print(f"결과 2 (FAIL 예상): {check_result([100, 100, 35])}")
print(f"결과 3 (FAIL 예상): {check_result([50, 50, 50])}")
