# [실습 4] 종합 성적 판독기 - 정답

def check_result(scores):
    # 1. 과락 확인 (리스트를 순회하며 40점 미만이 있는지 검사)
    for score in scores:
        if score < 40:
            return "FAIL" # 과락 발견 즉시 함수 종료 및 FAIL 반환
    
    # 2. 평균 계산
    avg = sum(scores) / len(scores)
    
    # 3. 평균 조건 검사
    if avg >= 60:
        return "PASS"
    else:
        return "FAIL"

# 호출 결과 확인
print(check_result([80, 90, 75]))   # PASS
print(check_result([100, 100, 35]))  # FAIL
print(check_result([50, 50, 50]))    # FAIL
