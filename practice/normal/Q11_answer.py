# 학생들의 이름과 시험 점수가 2차원 리스트로 주어집니다.
# 점수가 두 번째로 높은 학생(들)의 이름을 리스트 형태로 출력하시오.
# (점수가 가장 높은 학생이 여러 명일 수 있으며, 두 번째로 높은 점수도 여러 명일 수 있습니다.)
scores = [['Kim', 88], ['Lee', 95], ['Park', 92], ['Choi', 85], ['Jung', 95], ['Kang', 92]]

# 1. 모든 점수를 수집하여 내림차순 정렬 후 중복 제거
all_scores = []
for score in scores:
    all_scores.append(score[1])

# set을 이용해 중복 제거 후 리스트 변환하여 정렬
unique_scores = sorted(list(set(all_scores)), reverse=True)

# 2. 두 번째로 높은 점수 확인
if len(unique_scores) >= 2:
    second_highest = unique_scores[1]
    
    # 3. 해당 점수를 가진 학생들 찾기
    runner_up_students = []
    for student_score in scores:
        if student_score[1] == second_highest:
            runner_up_students.append(student_score[0])
            
    print(runner_up_students)  # ['Park', 'Kang']
else:
    print("두 번째 높은 점수가 없습니다.")
