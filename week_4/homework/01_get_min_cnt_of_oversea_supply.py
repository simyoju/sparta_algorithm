import heapq

ramen_stock = 4 # 밀가루 수량
supply_dates = [4, 10, 15] # 밀가루 공급 일정
supply_supplies = [20, 5, 10] # 공급가능한 밀가루 수량
supply_recover_k = 30 # 원래 공장으로부터 공급받을 수 있는 시점



def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    cnt = 0
    need = k-stock

    # goal: 현재 stock > k
    # 공장이 멈추지 않아야하기 때
    while stock < k:
        return
    return cnt


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))