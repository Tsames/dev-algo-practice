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


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        # Mimic a hashmap that counts the number of occurrences of each lower case letter
        # Using 0's for all letters that don't occur
        countS1, countS2 = [0] * 26, [0] * 26

        # Fill up our lists with the length of s1
        # this will be our window that we shift
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        # Iterate 26 times, to figure out the starting match count between the two lists
        matches = 0
        for j in range(26):
            matches += 1 if countS1[j] == countS2[j] else 0

        print(f"Matches is {matches} before adjustment")
        # Iterate through s2, adjusting matches at each iteration
        l = 0
        for r in range(len(s1), len(s2)):
            # If we ever find that matches = 26, then we return True. Otherwise, we return False.
            # This is because our count of s2 is only for a window of size s1.
            # So if the two arrays are equal, then they are anagrams.
            if matches == 26: return True

            # Next we adjust matches for the right index of the window
            idx_right = ord(s2[r]) - ord('a')
            countS2[idx_right] += 1
            # If they are equal we know we just found a new match
            if countS2[idx_right] == countS1[idx_right]:
                matches += 1
            # If they are within one, we know we just removed a match that was previously there
            elif countS1[idx_right] + 1 == countS2[idx_right]:
                matches -= 1

            # Then adjust matches for the left index of the window using the same logic
            idx_left = ord(s2[l]) - ord('a')
            countS2[idx_left] -= 1
            if countS2[idx_left] == countS1[idx_left]:
                matches += 1
            elif countS1[idx_left] + 1 == countS2[idx_left]:
                matches -= 1

            l += 1

        print(f"s1 count is:  {countS1}")
        print(f"s2 count is: {countS2}")
        print(f"matches is: {matches}")

        # If we get all the way through our loop, the last iteration might have got us to 26 matches
        return matches == 26


solution = Solution()

test_cases = [
    {
        "s1": "ab",
        "s2": "eidbaooo",
        "expected": True,
        "description": "Basic test with permutation present"
    },
    {
        "s1": "ab",
        "s2": "eidboaoo",
        "expected": False,
        "description": "Basic test with no permutation"
    },
    {
        "s1": "abc",
        "s2": "bbbca",
        "expected": True,
        "description": "Permutation at the end"
    },
    {
        "s1": "hello",
        "s2": "ooolleoooleh",
        "expected": False,
        "description": "Longer strings with similar characters"
    },
    {
        "s1": "adc",
        "s2": "dcda",
        "expected": True,
        "description": "Permutation at start"
    },
    {
        "s1": "a",
        "s2": "ab",
        "expected": True,
        "description": "Single character s1"
    },
    {
        "s1": "abc",
        "s2": "ccccbbbbaaaa",
        "expected": False,
        "description": "No consecutive permutation"
    },
    {
        "s1": "abbc",
        "s2": "babca",
        "expected": True,
        "description": "Test with duplicate characters"
    }
]

for i, test in enumerate(test_cases, 1):
    # Test the first implementation
    result = solution.check_inclusion(test["s1"], test["s2"])
    assert result == test["expected"], (
        f"Test {i} ({test['description']}) failed for check_inclusion. "
        f"Expected {test['expected']}, but got {result}"
    )

print("All tests passed!")
