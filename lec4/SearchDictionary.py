# -*- coding: utf-8 -*-

# python 2.7
#
# 例題 Search Dictionary
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C&lang=jp
# を解いた。
# 
# python の set を用いた。

import sys

s = set([])

n = int(raw_input());

for i in range(n):
    cmd = sys.stdin.readline().split()
    if  cmd[0] == "insert":
        s.add(cmd[1])
    else:
        if cmd[1] in s:
            print("yes")
        else:
            print("no")
