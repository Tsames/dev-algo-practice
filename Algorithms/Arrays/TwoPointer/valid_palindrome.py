"""
https://neetcode.io/problems/is-palindrome

Is Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non alpha numeric characters, and convert to lower case
        corrected_string = ""
        
        for char in s:
            if char.isalnum():
                corrected_string += char.lower()
        
        # Check each index against the index of the opposite side of the string
        left_pointer = 0
        right_pointer = len(corrected_string) - 1
        
        while left_pointer < right_pointer:
            if not corrected_string[left_pointer] == corrected_string[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        
        return True
    
    
# Test Cases
solution = Solution()
assert solution.isPalindrome("tab a cat") == False
assert solution.isPalindrome("Was it a car or a cat I saw?") == True

"""
Very simple example of a two pointer problem. Biggest thing I learned here was
how to remove all non-alphanumeric characters using .isalnum() and convert characters/strings
to all lower case using .lower().
"""