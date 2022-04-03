import sys

test_nums = int(sys.stdin.readline())
for i in range(1, test_nums+1):
    c1,m1,y1,k1 = tuple(map(int,sys.stdin.readline().split()))
    c2,m2,y2,k2 = tuple(map(int,sys.stdin.readline().split()))
    c3,m3,y3,k3 = tuple(map(int,sys.stdin.readline().split()))
    
    minc = min(c1,c2,c3)
    minm = min(m1,m2,m3)
    miny = min(y1,y2,y3)
    mink = min(k1,k2,k3)

    if minc+minm+miny+mink < 1000000:
        print(f"Case #{i}: IMPOSSIBLE")
    else:
        finalc = minc
        finalm = min(1000000-finalc, minm)
        finaly = min(1000000-finalc-finalm, miny)
        finalk = min(1000000-finalc-finalm-finaly,mink)
        print(f"Case #{i}: {finalc} {finalm} {finaly} {finalk}")