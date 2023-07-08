from collections import Counter
class Solution:
   def solve(self, s):
      c = Counter(s)
      count = 0
      for i in c.values():
         if i % 2 != 0:
            if count == 0:
               count += 1
               continue
            return False
      return True
ob = Solution()
s = "admma"
print(ob.solve(s))