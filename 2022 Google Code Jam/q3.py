import sys
from collections import deque

test_nums = int(sys.stdin.readline())
for i in range(1, test_nums+1):
    N = tuple(map(int,sys.stdin.readline().split()))
    dice = list(map(int,sys.stdin.readline().split()))
    dice.sort()

    dice = deque(dice)

    longest_straight = 0
    while dice:
        curr = dice.popleft()
        if longest_straight < curr:
            longest_straight += 1
        else: 
            pass
    print(f"Case #{i}: {longest_straight}")