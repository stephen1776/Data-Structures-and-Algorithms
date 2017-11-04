# python3
'''
Rope

Input Format. The first line contains the initial string 𝑆.
The second line contains the number of queries 𝑞.
Next 𝑞 lines contain triples of integers 𝑖, 𝑗, 𝑘.

Output Format. Output the string after all 𝑞 queries.
'''
import sys

class Rope:
	def __init__(self, s):
		self.s = s
	def result(self):
		return self.s
	def process(self, i, j, k):
		# Write your code here
		newString = self.s[i:j + 1]
		self.s = self.s[:i] + self.s[j + 1:]
		if k == 0:
			self.s = newString + self.s
		else:
			self.s =  self.s[:k] + newString + self.s[k:]

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
