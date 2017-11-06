'''
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2104
カントリー・ロードを解いた。

pdfのヒントを参考に、貪欲法と呼ばれる方法でといた。
隣接する家間の距離を長さで並べ替え、長い方から発電所を設置していく。
'''

t = int(input())
for i in range(t):
    n, k = map(int, input().split(" ")) 
    houses = [] 
    houses += map(int, input().split(" "))
    dist = [] 
    for j in range(len(houses) - 1):
        dist.append(houses[j+1] - houses[j])
    dist.sort() 
    #print(dist)
    wire = max(houses) - min(houses) 
 
    while(k > 1 and len(dist) > 0): #k が家の数に対して多い場合も考慮が必要
        wire -= dist.pop()
        k -= 1
    print(wire)
