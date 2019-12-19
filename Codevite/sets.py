from itertools import combinations

m,n=map(int,input().split(','))
s=set(map(int,input().split(',')))
subs=set(combinations(sorted(s), 3))
print(len(list(''.join(str(each)) for each in subs if sum(each)%n==0))%1009)
