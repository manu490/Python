import string
digs = string.digits + string.ascii_letters
def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)
  
N=int(input())
arr=list(map(int,input().split(',')))
nums=[]
for i in  arr:
  six=int2base(i, 6)
  y=0
  for i in six:
    y+=int(i)
  nums.append(y)
#print(nums)
count=0
for i in range(N):
  for j in range(i+1,N):
    #print(nums[i],nums[j])
    if nums[i]>nums[j]:
      count+=1
print(count)
