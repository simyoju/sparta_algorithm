shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def binary_search(target, array):
    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2
    return False

def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    shop_menus.sort()
    for order in orders:
        if not binary_search(order, shop_orders):
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)