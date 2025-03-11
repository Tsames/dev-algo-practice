'''
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

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


conditional check, if len(s) < 2, return len(s)

seen_before is our set()
longest is what we return
left pointer initialized to the 0th index of our string
right pointer initialized to the 1st index of our string

while loop where the left pointer is less than len(s) - 1
    if s[right pointer] is not in our set
        add it to our set
        move right pointer over
    if s[right pointer] is in our set
        if len(set) > longest:
            longest = len(set)
        seen_before = set()
        left_pointer = left_pointer + 1
        right_pointer = left_pointer + 1

return longest
'''

def longestSubstringBruteForce(s: str) -> int:
    if len(s) < 2:
        return len(s)

    seen_before = set()
    longest = 0

    left_pointer = 0
    right_pointer = 1

    while left_pointer < len(s):
        right_pointer = left_pointer
        seen_before.clear()

        while right_pointer < len(s):

            # If char at right pointer has not been seen before
            if s[right_pointer] not in seen_before:
                seen_before.add(s[right_pointer])
                right_pointer += 1

                longest = max(longest, len(seen_before))
            # If char at right pointer has been seen before
            else:
                break
        
        left_pointer += 1

    return longest

def longestSubstringFast(s: str) -> int:
    
    # declare our set
    seen = set()
    # declare our res
    res = 0
    # declare our left pointer
    l = 0
    
    # Iterate through each index of s, with a variable called r
    for r in range(len(s)):
        # If r is at an element that we've already encountered before
        while s[r] in seen:
        # Keep moving our left pointer over, and removing the element at each previous index left pointer was at until we have don't have
        # that conflicting duplicate anymore
            seen.remove(s[l])
            l += 1
        # Then add the new value to the set
        seen.add(s[r])
        # Update res if applicable
        res = max(res, r - l + 1)
        
    return res
    

assert longestSubstringBruteForce("abcabcbb") == 3, "Test Case 1 Failed"
assert longestSubstringBruteForce("bbbbb") == 1, "Test Case 2 Failed"
assert longestSubstringBruteForce("pwwkew") == 3, "Test Case 3 Failed"

assert longestSubstringFast("abcabcbb") == 3, "Test Case 4 Failed"
assert longestSubstringFast("bbbbb") == 1, "Test Case 5 Failed"
assert longestSubstringFast("pwwkew") == 3, "Test Case 6 Failed"