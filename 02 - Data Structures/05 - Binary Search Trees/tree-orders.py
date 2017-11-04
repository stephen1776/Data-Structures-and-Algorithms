# python3
'''
Binary tree traversals

Task. You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.

Input Format. The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
from 0 to 𝑛 − 1. Vertex 0 is the root.

Output Format. Print three lines. The first line should contain the keys of the vertices in the in-order
traversal of the tree. The second line should contain the keys of the vertices in the pre-order traversal
of the tree. The third line should contain the keys of the vertices in the post-order traversal of the tree.
'''
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def inOrderRecursive(root):
      if self.left[root] != -1:
        inOrderRecursive(self.left[root])
      self.result.append(self.key[root])
      if self.right[root] != -1:
        inOrderRecursive(self.right[root])
    inOrderRecursive(0)
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def preOrderRecursive(root):
      self.result.append(self.key[root])
      if self.left[root] != -1:
        preOrderRecursive(self.left[root])
      if self.right[root] != -1:
        preOrderRecursive(self.right[root])
    preOrderRecursive(0)
    return self.result


  def postOrder(self):
    self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
    def postOrderRecursive(root):
        if self.left[root] != -1:
            postOrderRecursive(self.left[root])
        if self.right[root] != -1:
             postOrderRecursive(self.right[root])
        self.result.append(self.key[root])

    postOrderRecursive(0)
    return self.result


def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
