'''
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2007
make purse light を解いた。

いいやり方が思いつかず、愚直で下手なコードを書いてしまった。
他の人のコードを見ると全然短くて、悲しくなったがとても勉強になった。
コードを書き始める前にもうちょっとよくアルゴリズムを考えるようにしようと思う。
'''

import math
i = 0
while(1):
    n = int(input())
    if n == 0: break
    if i == 1: print("")
    a,b,c,d = map(int, input().strip().split(' '))
    count10,count50,count100,count500 = 0,0,0,0
    #print('a,b,c,d,n = %d, %d, %d, %d ,%d' % (a,b,c,d,n)) 
    #10yen
    x = math.ceil((n%50)/10)
    if (x <= a):
        a -= x
        count10 += x
        n -= 10 * x
    while(a>= 5):
        a -= 5
        count10 += 5
        n -= 50
    #print('a,b,c,d,n = %d, %d, %d, %d ,%d' % (a,b,c,d,n)) 
    #50yen
    y = math.ceil((n%100)/50)
    if (y <= b):
        b -= y
        count50 += y
        n -= 50 * y
    while(b>= 2):
        b -= 2
        count50 += 2
        n -= 100
    #print('a,b,c,d,n = %d, %d, %d, %d ,%d' % (a,b,c,d,n))
    #100yen
    z = math.ceil((n%500)/100)
    if (z <= c):
        c -= z
        count100 += z
        n -= 100 * z
    while(c>= 5):
        c -= 5
        count100 += 5
        n -= 500
    #print('a,b,c,d,n = %d, %d, %d, %d ,%d' % (a,b,c,d,n))
    #500
    while(n>0):
        d -= 1
        count500 += 1
        n -= 500
    #print('a,b,c,d,n = %d, %d, %d, %d ,%d' % (a,b,c,d,n))
    #?????¨?????°?????????
    if (count10 > 0): print ('%d %d' % (10,count10))
    if (count50 > 0): print ('%d %d' % (50,count50))
    if (count100 > 0): print ('%d %d' % (100,count100))
    if (count500 > 0): print ('%d %d' % (500,count500))
    i = 1
