# python3
'''
Task. You are given a description of a rooted tree. Your task is to compute and output its height. Recall
that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.

Input Format. The first line contains the number of nodes 𝑛. The second line contains 𝑛 integer numbers
from −1 to 𝑛 − 1 — parents of nodes. If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root,
otherwise it’s 0-based index of the parent of 𝑖-th node. It is guaranteed that there is exactly one root.
It is guaranteed that the input represents a tree.

Output Format. Output the height of the tree.
'''
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.nodes = {}

        def compute_height(self):
                root = None
                try:
                        root = self.parent.index(-1)
                except ValueError:
                        return 0
                for i, j in enumerate(self.parent):
                        if (j == -1):
                                root = i
                                continue

                        if (j not in self.nodes):
                                self.nodes[j] = [i]
                        else:
                                self.nodes[j].append(i)
                queue = [(root, 1)]
                height = 1

                while (len(queue) > 0):
                        j, h = queue.pop()

                        if (j not in self.nodes):
                                continue

                        h += 1

                        if (h > height):
                                height = h

                        for i in self.nodes[j]:
                                queue.append((i, h))
                return height

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
