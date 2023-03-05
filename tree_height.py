# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function

    max_height = 0
    for v in range(n):
        height = 0
        cur = v 
        while cur != -1:
            height += 1
            cur = parents[cur]
        max_height = max(max_height, height)
    return max_height

def main():
    cmd = input()
    if "F" in cmd:
        file_path = input()
        path = "test/"+file_path
        if not "a" in file_path:
            text = open(path)
            text1 = text.read()
            text.close()
            sep = text1.partition("\n")
            n = int(sep[0])
            parents_1 = sep[2].split(" ")
            parents = ([int(x) for x in parents_1])
            print (compute_height(n, parents))
    elif "I" in cmd:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))

    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()