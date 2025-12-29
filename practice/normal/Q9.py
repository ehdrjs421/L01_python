# [실습 9]
# 다음 리스트에서 이메일 주소의 도메인(gmail.com, naver.com 등)만 추출하여 
# 중복을 제거한 뒤, 알파벳 순서대로 정렬된 리스트를 구하시오.
emails = ['abc@naver.com', 'def@gmail.com', 'ghi@naver.com', 'jkl@daum.net', 'mno@gmail.com']

# 로직 작성
domain = set()
for mail in emails:
    a = mail.split("@")
    domain.add(a[1])

unique_domains = sorted(list(domain))




print(unique_domains) # ['daum.net', 'gmail.com', 'naver.com']
