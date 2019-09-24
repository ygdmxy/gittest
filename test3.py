#文本进度条

import time

start = time.perf_counter()

scale = 50
print("执行开始".center(80,'-'))
for i in range(scale):
    a= '*'* i
    b='.' * (scale - i)
    c= (i/scale) * 100
    dur= time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)

'''
print("执行开始".center(80,'-'))
for j in range(101):    
    print("\r{:3}%".format(j),end='')
    time.sleep(0.1)


'''

end = time.perf_counter()
print()

print(" 程序用时：{:.3f}".format(end - start) )