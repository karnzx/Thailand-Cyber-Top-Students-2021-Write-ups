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

# flag = input('Flag: ')
# num = 1
# x = next(500)
# for c in flag:
#     num = num * x + ord(c)
#     x = next(x)
# print(num)

# data = 20180563089871994563922278132178649747876754717401400842606646900649623354628170931148188497310312646743702

# data = 281017
# data = 43606642979505
# data = 4043283096665012274212788
data = 20180563089871994563922278132178649747876754717401400842606646900649623354628170931148188497310312646743702
import time


xx = []

x = next(500)
xx.append(x)



# while True:
#     x = next(x)
#     check = data % x
#     print('->', data % x)
#     xx.append(x)

#     print(xx)
#     print(check % 2 )
#     # if check < 128:
#         # break

#     time.sleep(1)

for i in range(50):
    x = next(x)
    xx.append(x)

print(xx)

for i in range(len(xx), 0, -1):
    text = ''
    cdata = data
    # print(i, list(reversed(xx[:i])))
    for x in reversed(xx[:i]):
        ch = cdata % x
        text = chr(ch) + text
        cdata = (cdata - ch ) // x
    print(f'"{text}"')