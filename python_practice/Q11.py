# 학생들의 이름과 시험 점수가 2차원 리스트로 주어집니다.
# 점수가 두 번째로 높은 학생(들)의 이름을 리스트 형태로 출력하시오.
# (점수가 가장 높은 학생이 여러 명일 수 있으며, 두 번째로 높은 점수도 여러 명일 수 있습니다.)
scores = [['Kim', 88], ['Lee', 95], ['Park', 92], ['Choi', 85], ['Jung', 95], ['Kang', 92]]

# 로직 작성
score = set(score[1] for score in scores)
score_sort = sorted(list(score))
# score_sort = [90]
if len(score_sort) < 2:
    runner_up_students = "두번째로 높은 점수는 없습니다."
else:
    second_score = score_sort[-2]
    runner_up_students = [name[0] for name in scores if name[1] == second_score]

print(runner_up_students,second_score) # ['Park', 'Kang']
