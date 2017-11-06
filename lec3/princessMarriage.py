'''
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2019
Princess' marriage を解いた。

襲われる期待値が大きいところから、金がなくなるまでガードを雇う場所を決めていく。
並び替えがかぎだった。
'''

while(True):
        n, m = map(int, input().split(" "))
        if(n == 0 and m == 0):
            break
        dp = []
        for i in range(n):
            dp.append(list(map(int, input().split(" "))))
        dp.sort(key = lambda x: x[1])
        dp.reverse()
 
        S = 0; #はじめはガードを雇わないときの襲われる期待値。雇うのに応じて減らす。
        for i in range(n):
            S += dp[i][0] * dp[i][1]
 
        for i in range(n):
            if (n <= 0):
                break
            guarded = min(m, dp[i][0])
            S -= dp[i][1] * guarded
            m -= guarded
        print(S)
