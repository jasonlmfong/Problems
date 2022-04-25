import sys

class Module(object):
    def __init__(self, fun = 0, obj = None):
        self.fun = fun
        self.pointer = obj

    def fun_sum(self):
        sum = self.fun
        if self.pointer:
            sum += self.pointer.fun_sum() #recursively
        return sum

test_nums = int(sys.stdin.readline())
for i in range(1, test_nums+1):
    N = int(sys.stdin.readline().split())
    Fun = list(map(int,sys.stdin.readline().split()))
    Pointers = list(map(int,sys.stdin.readline().split()))

    modules = {0:Module(0)}
    for j in range(len(Fun)):
        modules[j+1] = Module(Fun[j], modules[Pointers[j]])

    initiators = []
    for k in range(1, len(Fun)+1):
        if k not in Pointers:
            initiators.append(k)

    max_fun = 0
    for l in initiators: 
    #something magical to run through each of the possible paths started by an initiator
        void = [0]
        fun_sum = modules[l].fun_sum()
        void.append(l)#and everything the recursion runs through
        max_fun = max(max_fun, fun_sum)

    print(f"Case #{i}: {max_fun}")