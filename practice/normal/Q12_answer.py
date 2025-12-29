# 데이터 분석 전, 결측치(None)를 처리하려고 합니다.
# 주어진 리스트에서 None을 제외한 숫자들의 평균을 구하고,
# 리스트 내의 모든 None을 해당 평균값으로 대체(반올림하여 정수로)한 뒤 
# 최종 리스트의 합계를 구하시오.
data = [10, 20, None, 30, 40, None, 50]

# 1. None을 제외한 숫자들의 합과 개수 구하기
valid_data = []
for x in data:
    if x is not None:
        valid_data.append(x)

# 2. 평균 구하기
avg = sum(valid_data) / len(valid_data)
# 반올림하여 정수로 변환
avg_int = int(round(avg))

# 3. None을 평균값으로 대체
cleaned_data = []
for x in data:
    if x is None:
        cleaned_data.append(avg_int)
    else:
        cleaned_data.append(x)

# 4. 합계 출력
total_sum = sum(cleaned_data)
print(total_sum)  # 210
