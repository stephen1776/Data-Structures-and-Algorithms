# python3
'''
Input Format. The first line of the input contains single integer 𝑛. The next line contains 𝑛 space-separated
integers 𝑎𝑖.

Output Format. The first line of the output should contain single integer 𝑚 — the total number of swaps.
𝑚 must satisfy conditions 0 ≤ 𝑚 ≤ 4𝑛. The next 𝑚 lines should contain the swap operations used
to convert the array 𝑎 into a heap.

What to Do
Change the BuildHeap algorithm from the lecture to account for min-heap instead of max-heap and for
0-based indexing.
'''

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [-1]
    self._data += [int(s) for s in input().split()]
    assert n == len(self._data) - 1

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def LeftChild(i):
    return 2 * i

  def RightChild(i):
    return 2 * i + 1

  def SiftDown(self, i):
    min_index = i
    left = HeapBuilder.LeftChild(i)
    right = HeapBuilder.RightChild(i)

    if left <= len(self._data) - 1 and self._data[left] < self._data[min_index]:
      min_index = left
    if right <= len(self._data) - 1 and self._data[right] < self._data[min_index]:
      min_index = right

    if i != min_index:
      self._swaps.append((i - 1, min_index - 1))
      self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
      self.SiftDown(min_index)

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
     #for i in range(len(self._data)):
    #   for j in range(i + 1, len(self._data)):
    #     if self._data[i] > self._data[j]:
    #       self._swaps.append((i, j))
    #       self._data[i], self._data[j] = self._data[j], self._data[i]
      for i in range((len(self._data) - 1) // 2, 0, -1):
        self.SiftDown(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
