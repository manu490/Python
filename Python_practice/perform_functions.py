# Problem Statement:
# Refer https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int, input().split()))
ops_num=int(input())
count=0
while count< ops_num:
    ops=str(input())
    eval('s.{0}({1})'.format(*ops.split()+['']))
    count=count+1
    continue
print(sum(s))
