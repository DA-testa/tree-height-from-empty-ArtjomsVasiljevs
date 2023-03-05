# python3

import sys
import threading
import numpy



def build_tree(n, parents):
    tree = {}
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            if parent not in tree:
                tree[parent] = []
            tree[parent].append(i)
    return tree, root


def compute_height(tree, root):
    if root not in tree:
        return 0
    height = 0
    for child in tree[root]:
        height = max(height, compute_height(tree, child))
    return height + 1 

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
            
            tree, root = build_tree(n, parents)
            height = compute_height(tree, root)
            print(height + 1)
            
    elif "I" in cmd:
        n = int(input())
        parents = list(map(int, input().split()))
        tree, root = build_tree(n, parents)
        height = compute_height(tree, root)
        print(height + 1)
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
