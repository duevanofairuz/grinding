from decimal import Decimal, getcontext, ROUND_DOWN

m, n, k = input().split()
k = int(k)

if k == 0:
    res = Decimal(m) / Decimal(n)
    print("{:.{}f}".format(res, k))
elif k!=0: 
    getcontext().prec = k + 50  # add extra buffer to precision
    getcontext().rounding = ROUND_DOWN  # round down to fix input 2 3 2, instead of 0.67, it would be 0.66
    res = Decimal(m) / Decimal(n)

    print("{:.{}f}".format(res, k))