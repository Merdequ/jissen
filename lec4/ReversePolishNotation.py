# -*- coding: utf-8 -*-

# python 2.7
#
# 例題 Reverse Polish Notation
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A&lang=jp
# を解いた。
# 
# スタックの使い方の練習

inputs = raw_input().split()
inputs.reverse() 
s = []

while (inputs != []): 
    a = inputs.pop()
    if (a == "+"):
        s.append(s.pop() + s.pop())
    elif (a == "-"):
        s.append(- s.pop() + s.pop())
    elif (a == "*"):
        s.append(s.pop() * s.pop())
    else:
        s.append(int(a))
print s.pop()

        
        
