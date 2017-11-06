# -*- coding: utf-8 -*-

# python 2.7
#
# 例題 Priority Queue
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
# を解いた。
# 
# 優先度つきキュー
# 大きい要素から順に取り出す
#
# heapq をimportすれば優先度付きキューが使えるのだが、
# heappopが最小の要素を取り出す仕様で、
# 今回の問題には都合が悪いのでsortを使ったところ、
# time limit exceededになって通らなかった。(最後のテストデータのサイズが結構大きい)
# 反数をとってheapqを使うと間に合った。(6.56秒)
# リストを全部並びけるような不要で時間がかかる処理をしていると今後は時間が足りなくなるかもしれない
# オンラインジャッジの早い人の解答はimportではなく標準入力のreadlineを使っていた(キューの実装は多分同じ)


import heapq
Q = []

while(1):
    a = raw_input().split()
    if a[0] == "end" :
        break
    elif a[0] == "insert":
        heapq.heappush(Q,- int(a[1]))
    elif a[0] == "extract":
        print - heapq.heappop(Q)
