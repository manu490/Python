"""Input Format:
For Full problem refer link:
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
The first line contains an integer , the number of test cases.
  Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of the queue.
Output Format:
Print an integer denoting the minimum number of bribes needed to get the queue into its final state.
Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people. """

#code
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps=0
    swaped=False
    lth=len(q)-1
    for c,v in enumerate(q):
        if (v-1)-c >2:
            return "Too chaotic"
    for i in range(lth):
        for j in range(lth):
            if q[j]>q[j+1]:
                temp=q[j]
                q[j],q[j+1]=q[j+1],temp
                swaps+=1
                swaped=True
        if swaped:
            swaped=False
        else:
            break
    return swaps




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
