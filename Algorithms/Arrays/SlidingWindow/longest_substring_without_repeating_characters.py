'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        '''
        Strategy:

        Declare a variable, res, to hold the length of the longest substring.
        Since we cannot have duplicate characters within a substring, we'll want to declare a set, seen, to keep track of the
        characters we have already come across.
        We'll also want to declare a left and right pointer, l and r, initially set to 0.

        We iterate within a while loop until r is out of bounds.

            If the element at index r is already in seen, we have a problem.
            We need to remove all instances of it in our substring.
            So, walk l forwards until that letter is no longer in seen.

            Add the element at index r to seen.
            Then set res equal to the length of seen if the length of seen is larger than res.

        Finally, once we are done iterating, we can return res.
        '''
        res = 0
        seen = set()
        l = r = 0

        while r < len(s):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            res = max(res, len(seen))
            r += 1

        return res

solution = Solution()
assert solution.length_of_longest_substring("abcabcbb") == 3, "Test one failed."
assert solution.length_of_longest_substring("bbbbb") == 1, "Test two failed."
assert solution.length_of_longest_substring("pwwkew") == 3, "Test three failed."


