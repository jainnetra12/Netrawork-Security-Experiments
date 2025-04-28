def chinese_remainder(n, a):
    sum = 0
    prod = 1
    for ni in n:
        prod *= ni
    for ni, ai in zip(n, a):
        p = prod // ni
        sum += ai * pow(p, -1, ni) * p
    return sum % prod

n = list(map(int, input("Enter moduli separated by space: ").split()))
a = list(map(int, input("Enter remainders separated by space: ").split()))
result = chinese_remainder(n, a)
print("x =", result)
