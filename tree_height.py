# python3

import sys
import threading
import numpy

class nodes:
    def __init__(self, parent, child=None):
        self.parent = parent
        self.child = child

    def add(self, node):
        if self.child is None:
            self.child = []
        self.child.append(node)

def compute_height(node):
    # Write this function
    if node.child is None:
        return 0
    child1 = node.child
    heightlist = []
    for child in child1:
        heightlist.append(compute_height(child))
    return max(heightlist, default=0)+1

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
            node_l = []
            for i in range(n):
                node_l.append(nodes(parents[i]))
            for child_index in range(n):
                parent_index = parents[child_index]
                if parent_index == -1:
                    root = child_index
                else:
                    node_l[parent_index].add(node_l[child_index])

            if len(node_l) == 0:
                return 0
    
            height = compute_height(node_l[root]) + 1
    
            print(height)

    elif "I" in cmd:
        n = int(input())
        parents = list(map(int, input().split()))
        node_l = []
        for i in range(n):
                node_l.append(nodes(parents[i]))
        for child_index in range(n):
            parent_index = parents[child_index]
            if parent_index == -1:
                root = child_index
            else:
                node_l[parent_index].add(node_l[child_index])

        if len(node_l) == 0:
            return 0
    
        height = compute_height(node_l[root]) + 1
    
        print(height)

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