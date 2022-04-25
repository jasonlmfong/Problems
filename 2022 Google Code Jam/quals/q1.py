import sys

test_nums = int(sys.stdin.readline())
for i in range(1, test_nums+1):
    R,C = tuple(map(int,sys.stdin.readline().split()))
    print("Case #%d:" %i)
    start_line = "..+"
    div_line = "+-+"
    first_hole = "..|"
    sub_hole = "|.|"
    for col in range(C - 1):
        start_line += "-+"
        div_line += "-+"
        first_hole += ".|"
        sub_hole += ".|"
    print(start_line)
    print(first_hole)
    print(div_line)
    for row in range(R-1):
        print(sub_hole)
        print(div_line)