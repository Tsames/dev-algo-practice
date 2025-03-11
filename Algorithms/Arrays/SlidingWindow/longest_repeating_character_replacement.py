'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/

424. Longest Repeating Character Replacement
You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        '''
        This problem in essence wants us to find the longest substring containing only a single letter, with k exceptions.
        Put another way, if we use a set to keep track of the letters we've encountered, that set cannot be greater than K + 1 length.
        That's not quite accurate, because the set only keeps track of the types of letters we've encountered, not the number of times we've encountered them.

        Could we use a hashmap instead? A hashmap does have the advantage of allowing us to keep track of the number of times
        we've seen a given character. It also has the downside that its not obvious if we've reached k exceptions.
        To know that we have to loop through the keys of the hashmap.

        The tricky part here is that the character that doesn't count against our exceptions can change during the middle of our iterations.
        Can we use a variable to keep track of the number of exceptions we've run into? This on its own isn't enough.
        Once we switch letters and start moving our left pointer over, we won't know how many exceptions the current subarray has.
        Or would we?

        The length of our substring is r - l + 1, where r is the right pointer and l is the left pointer.
        Lets call this length s.
        If we know that s includes k exceptions (because we ran into a new character).
        Then we know that the number of letters of the same type is s - k.
        So when we hit a new letter, and we want to move the left pointer over, each time we would be decrementing s - k.
        But even this becomes problematic when there are many different types of letters in our string.

        ----------------------------------------

        We want to use a hashmap to store the number of times we've seen a given character.
        Our hash map will have a max length of 26, since there are 26 unique characters in the english language.

        We iterate through our list using left and right pointers.
        Each iteration, we increment the count of the element at the right pointer in our hashmap (or add it).
        Then, we calculate the number of times the most frequent character in our window has occurred.
        If the length of our window, r - l + 1, minus the number of occurrences of the most frequent character is less
        than or equal to k, then we have a valid substring.
        If we don't, we need to move our left pointer over and check again.

        The space complexity would be O(26) which is just O(1).
        The time complexity would be O(26 * n) which is just O(n).
        '''
        res = 0
        hash = {}

        l = 0
        for r in range(len(s)):
            hash[s[r]] = 1 + hash.get(s[r], 0)

            while (r - l + 1) - max(hash.values()) > k:
                hash[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

solution = Solution()
assert solution.character_replacement("ABAB", 2) == 4, "Test one failed"
assert solution.character_replacement("AABABBA", 1) == 4, "Test two failed"
assert solution.character_replacement("ABBCDAABBDDC",2) == 4, "Test two failed"
