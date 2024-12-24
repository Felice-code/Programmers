def solution(chicken):
    service_chickens = 0
    coupons = chicken

    while coupons >= 10:
        new_chickens = coupons // 10 
        service_chickens += new_chickens 
        coupons = (coupons % 10) + new_chickens  

    return service_chickens
