# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
H = open('f.txt','r')
for line in H:
    print(line)
H.close()

with open ('f.txt','r') as S:
    for line in S:
        print(line)