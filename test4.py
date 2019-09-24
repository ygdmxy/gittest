
#import random
'''random.seed(10)
print(random.getrandbits(16))

for c in "python123":
    if c=='t':
        break
    print(c,end='')
'''

'''def fact(n):
    s=1
    for i in range(1,n+1):
        s = s*i
    return s
'''
def fact(n):
    if n<=1: return 1
    else:
        return n*fact(n-1)
print(fact(100))