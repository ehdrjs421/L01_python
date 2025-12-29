# 다음 리스트에서 이메일 주소의 도메인(gmail.com, naver.com 등)만 추출하여 
# 중복을 제거한 뒤, 알파벳 순서대로 정렬된 리스트를 구하시오.
emails = ['abc@naver.com', 'def@gmail.com', 'ghi@naver.com', 'jkl@daum.net', 'mno@gmail.com']

# 1. 도메인 추출
domains = []
for email in emails:
    domain = email.split('@')[1]
    domains.append(domain)

# 2. 중복 제거
unique_domains = list(set(domains))

# 3. 정렬
unique_domains.sort()

print(unique_domains)  # ['daum.net', 'gmail.com', 'naver.com']
