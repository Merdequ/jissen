# -*- coding: utf-8 -*-

# python 2.7
#
# 例題 Round-Robin Scheduling
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_ B&lang=jp
# を解いた。
# 
# 今回はキューを使う

import collections


qu = collections.deque()
n, q = map(int, raw_input().split())
t = 0


for i in range(n):
    name, timestr = (raw_input().split())
    qu.append([name, int(timestr)])

while len(qu) > 0:
    p = qu.popleft()
    if p[1] <= q: # プロセスの残り時間がクオンタム以下のとき
        t += p[1]
        print p[0], t
    else:
        t += q
        p[1] -= q
        qu.append(p)

        
        
