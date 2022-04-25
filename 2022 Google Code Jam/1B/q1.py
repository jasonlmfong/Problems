import sys
from collections import deque

test_nums = int(sys.stdin.readline())
for i in range(1, test_nums+1):
    dequesize = int(sys.stdin.readline())
    pancakes = deque(list(map(int,sys.stdin.readline().split())))
    
    #the most delicious one served so far
    max_deli = 0

    #number of paying customers
    num_pay = 0

    for j in range(dequesize):
        if len(pancakes) == 1:
            new = pancakes.pop()
            if max_deli <= new:
                num_pay += 1
                max_deli = new
            break
        
        left = pancakes.popleft()
        right = pancakes.pop()
        if left <= right:
            new = left
            pancakes.append(right)
            if max_deli <= new:
                num_pay += 1
                max_deli = new
        if left > right:
            new = right
            pancakes.appendleft(left)
            if max_deli <= new:
                num_pay += 1
                max_deli = new

    print(f"Case #{i}: {num_pay}")