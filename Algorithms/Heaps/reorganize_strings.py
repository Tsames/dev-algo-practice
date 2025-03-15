'''
https://leetcode.com/problems/reorganize-string/description/

767. Reorganize String
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
'''
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
       count = Counter(s)
       max_heap = [(-cnt, char) for char, cnt in count.items()]
       heapq.heapify(max_heap)

       prev = None
       res = ""
       while max_heap or prev:
           # We know we have an invalid string if our max heap is empty
           # but there is still something in prev,
           # meaning we have no other characters to choose from except the character we just used
           if prev and not max_heap:
               return ""

           # Get the most frequent char besides prev
           cnt, char = heapq.heappop(max_heap)
           res += char
           cnt += 1

           if prev:
               heapq.heappush(max_heap, prev)
               prev = None
           if cnt != 0:
               prev = (cnt, char)
       return res

solution = Solution()

# Test case 1
expected = "aba"
actual = solution.reorganizeString("aab")
assert actual == expected, f"Test one failed. Expected: {expected}, but got: {actual}"

# Test case 2
expected = ""
actual = solution.reorganizeString("aaab")
assert actual == expected, f"Test two failed. Expected: {expected}, but got: {actual}"

print("All tests passed!")

