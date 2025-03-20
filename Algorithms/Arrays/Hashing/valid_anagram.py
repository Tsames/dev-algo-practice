'''
https://leetcode.com/problems/valid-anagram/description/

Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

class Solution:
    def isAnagramSort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagramHash(self, s: str, t: str) -> bool:
        hash1, hash2 = dict(), dict()
        for c in s:
            hash1[c] = 1 + hash1.get(c, 0)
        for c in t:
            hash2[c] = 1 + hash2.get(c, 0)

        return hash1 == hash2

solution = Solution()
assert solution.isAnagramSort("anagram", "nagaram") == True, "Test one failed."
assert solution.isAnagramSort("rat", "car") == False, "Test two failed."
assert solution.isAnagramSort("", "aaa") == False, "Test three failed."
assert solution.isAnagramSort("aaa", "") == False, "Test four failed."
print("All tests for isAnagramSort have passed!")

assert solution.isAnagramHash("anagram", "nagaram") == True, "Test one failed."
assert solution.isAnagramHash("rat", "car") == False, "Test two failed."
assert solution.isAnagramHash("", "aaa") == False, "Test three failed."
assert solution.isAnagramHash("aaa", "") == False, "Test four failed."
print("All test for isAnagramHash have passed!")