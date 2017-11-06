# -*- coding: utf-8 -*-

# python 2.7
#
# 例題 English sentence
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0029
# を解いた。
# 
# 文字列のリストに対し、max 関数をkeyにcountとlenを用いて使うことで、
# 出現頻度最大のものと長さ最大のものを求める。
# 


s = raw_input().split()
mcount = max(s, key = lambda x: s.count(x))
mlen = max(s, key = lambda x: len(x))
print mcount, mlen
