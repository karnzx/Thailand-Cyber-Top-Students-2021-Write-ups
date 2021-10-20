
def check(a1):
    v5 = 0
    v4 = 1
    v3 = 0
    
    i = 2
    while(i<a1):
        v3 = v4 + v5
        v5 = v4
        v4 = v3

        i += 1

    return v3

def decheck(ans):
    
    v5 = 0
    v4 = 1
    v3 = 0
    
    i = 2
    while True:
        v3 = v4 + v5
        v5 = v4
        v4 = v3

        i += 1
        if v3 == ans:
            break

    return i-1




key = [0x35C7E2, 0x452F, 0x2547029, 0x1A6D, 0x1FC6E116668E68, 0x59, 0x207FD8B6AD, 0x90, 0x0D, 8,2,2,
        0x59, 0x8, 0x90, 0x15, 0x0C69E60A65, 0x90, 0x37, 0x90, 0x0D, 0x59, 0x0C69E60A65,
        0x3495CB62F5, 0x0D, 3, 8, 0x1415F2AC48, 0x8, 0x0C69E60A65, 0x59, 0x90, 0x5, 0x207FD8B6AD, 0x59,
        0x22, 0x7AC0CA1E3, 0x533163EF0321E5]

# test = 'abc'
# for i in test:
#     print((check(ord(i) - 45)))

print(len(key))

flag = ''
for k in key:
    x = decheck(k)
    # print(k, x)
    flag += chr(x+45)


print(flag)
print(len(flag))
