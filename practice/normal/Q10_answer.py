# [실습 10]
# 다음과 같이 일자별 판매 기록이 리스트로 주어질 때, 
# 각 아이템별 총 판매 금액을 딕셔너리 형태로 구하시오.
sales = [
    {'item': 'Apple', 'price': 1000}, 
    {'item': 'Banana', 'price': 500}, 
    {'item': 'Apple', 'price': 1200}, 
    {'item': 'Grape', 'price': 2000}, 
    {'item': 'Banana', 'price': 600}
]

total_sales = {}

for sale in sales:
    item = sale['item']
    price = sale['price']
    
    if item in total_sales:
        total_sales[item] += price
    else:
        total_sales[item] = price

print(total_sales)  # {'Apple': 2200, 'Banana': 1100, 'Grape': 2000}

# setdefault를 사용하는 방식
# total_sales = {}
# for sale in sales:
#     total_sales.setdefault(sale['item'], 0)
#     total_sales[sale['item']] += sale['price']
