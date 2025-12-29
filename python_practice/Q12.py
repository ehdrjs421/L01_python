# 데이터 분석 전, 결측치(None)를 처리하려고 합니다.
# 주어진 리스트에서 None을 제외한 숫자들의 평균을 구하고,
# 리스트 내의 모든 None을 해당 평균값으로 대체(반올림하여 정수로)한 뒤 
# 최종 리스트의 합계를 구하시오.
data = [10, 20, None, 30, 40, None, 50]

# 로직 작성
total_sum = 0
sums = 0
check = 0
for num in data:
    if num != None:
        sums += num
        check += 1
ave = int(sums/check)

for i in range(len(data)):
    if data[i] == None:
        data[i] = ave
total_sum = sum(data)


print(total_sum) # 210 (평균이 30이므로 None 2개가 30으로 바뀌어 합계 210)
