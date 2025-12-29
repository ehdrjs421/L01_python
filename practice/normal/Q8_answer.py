# [실습 8] 도서 인기 순위 정렬 - 정답

books = [
    {'title': '파이썬 기초', 'loans': 45, 'year': 2021},
    {'title': '데이터 분석 실무', 'loans': 72, 'year': 2023},
    {'title': '머신러닝 입문', 'loans': 45, 'year': 2022},
    {'title': '딥러닝 가이드', 'loans': 72, 'year': 2021},
    {'title': '통계학의 이해', 'loans': 30, 'year': 2020}
]

# 람다 함수를 사용한 다중 조건 정렬
# -를 붙이면 내림차순(오름차순의 반대)으로 동작합니다.
sorted_books = sorted(books, key=lambda x: (-x['loans'], -x['year']))

# 결과 출력
for book in sorted_books:
    print(f"{book['title']} (대출: {book['loans']}, 연도: {book['year']})")

# [결과]
# 데이터 분석 실무 (대출: 72, 연도: 2023)
# 딥러닝 가이드 (대출: 72, 연도: 2021)
# 머신러닝 입문 (대출: 45, 연도: 2022)
# 파이썬 기초 (대출: 45, 연도: 2021)
# 통계학의 이해 (대출: 30, 연도: 2020)
