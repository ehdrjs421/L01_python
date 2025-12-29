# [실습 3]
# 주어진 배열 안의 값을 전부 2배로 만드시오.
# ex) [7, 2, 3]의 경우 [14, 4, 6]이 되어야 합니다.
nums = [7, 2, 9, 8, 4, 3, 5]

for i in range(len(nums)):
    nums[i] *= 2
    
print(nums)