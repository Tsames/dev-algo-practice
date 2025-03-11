'''
https://leetcode.com/problems/permutation-in-string/description/

567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
from collections import Counter

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        '''
        This problem seems like two smaller problems.
        First we need to slide a window through s2 of size s1.
        Then we need to check if the window contains a permutation of s1.

        We've checked whether one string is a permutation of another string in the past by sorting.
        But sorting all substrings of size s1 in s2 is expensive.
        The other method we can use is a hashmap to count all the occurrences of all the characters in s1.

        ---------

        Let's start with by declaring two hash maps, hash1 and hash2, as well as a left pointer, l.
        Count the characters in s1, by filling in hash1.

        Then iterate over each character of s2 with an index, r (our right pointer).

            On each iteration, we check:
            If s2 @ r is not in hash1. If it's not in hash1, then it's a letter that's not in s1.
            So we need to move our left pointer to r + 1, and reset hash2.

            If s2 @ r is in hash1, then we need to check if the counts are the same.
            If the count is smaller in hash2, all we need to do is increment the count in hash2.

            If s2 @ r is in hash1 and the count is already equal, then we need to move our left pointer over
            until the count of s2 @ r in hash2 is either less than that of hash1 or l is equal to r.



        if s2[r] is in hash1, then check if their counts are the same.
        If their counts are the same and the length of hash2 is the same as the length of s1, break and return true.

        if s2[r] is in hash1, and their counts
        '''
        hash1, hash2 = {}, {}
        for s in s1:
            hash1[s] = 1 + hash1.get(s, 0)

        l = 0
        for r in range(len(s2)):
            c = s2[r]

            if c not in hash1:
                l = r + 1
                hash2 = {}
                continue

            hash2[c] += 1

            while (hash2[c] > hash1[c] and l <= r) or len(hash2) > len(s1):
                hash2[s2[l]] -= 1
                l += 1

            if len(hash2) == len(s1):
                return True

            if len(hash2) > len(s1):







solution = Solution()
assert solution.check_inclusion("ab", "eidbaooo") == True, "Test one failed"
assert solution.check_inclusion("ab", "eidboaoo") == False, "Test two failed"
