while True:
    try:
        n, k = map(int, input().split())
        coupon = n
        stamp = 0
        chicken = 0
        while coupon > 0:
            chicken += coupon
            stamp += coupon
            coupon = stamp // k
            stamp = stamp % k
        print(chicken)
    except:
        break