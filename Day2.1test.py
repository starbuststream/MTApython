# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

totalscore = []
while True:  #一直進入迴圈模式
    score=int(input("分數"))
    if score=="999":
        break #直到碰到break才跳出迴圈
    else:
        totalscore.append(score)
        xscore = sorted(totalscore,reverse = True)
   #     totalscore.sort()#小到大排列
      #  totalscore.reverse() #反過來，變大到小
    print(xscore)
    
    
 