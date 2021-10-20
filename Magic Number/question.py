def next(n):
    while True:
        n = n + 1
        c = 0
        for i in range(2, n // 2):
            if n % i == 0:
                c += 1
                break
        if c == 0:
            return n

flag = input('Flag: ')
num = 1
x = next(500)    
for c in flag:
    num = (num * x) + ord(c)
    c  = num_new - (num_old * x)
    x = next(x)
print(num)

# 20180563089871994563922278132178649747876754717401400842606646900649623354628170931148188497310312646743702
