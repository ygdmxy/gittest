import matplotlib.pyplot as plt
from itertools import permutations
import time
import matplotlib
 
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = 'SimHei'
 
def baolimeijufa(ls1, ls2):
    tp2 = tuple(ls2)
    all_ls1 = permutations(ls1)
    flag = False
    for s in all_ls1:
        if s == tp2:
            flag = True
    return flag
ls_flag = []
ls_time = []
for n in range(1,11):
    start = time.perf_counter()
    ls1 = [ i for i in range(10, 10+n)]
    ls2 = [ i for i in range(n)]
    ls_flag.append(baolimeijufa(ls1, ls2))
    ls_time.append(time.perf_counter() - start)
 
# print(ls_flag)
# print(ls_time)
 
plt.figure(figsize=(8,6))
plt.plot(list(range(1,11)), ls_time, 'ro-')
plt.xlabel('规模(n)');plt.ylabel('时间(s)')
plt.xticks(range(1,11), range(1,11))
plt.show()