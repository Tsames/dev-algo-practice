'''
https://neetcode.io/problems/anagram-groups

49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
       '''
       In valid_anagram we handled the identification of an anagram by either
            a. Sorting the strings and then comparing them
            b. Creating a hashmap counter of both strings and then comparing those hashmaps

       One method that we could use would be to declare a hashmap to store all strings that are anagrams of each other.
       The value for this hashmap would be a list.
       The key would be the sorted string.
       Then we would a list with each value from our hashmap inside of it.

       This solution would be O(n * log(n)) [from sorting] where n is the average length of the strings in strs
       Multiplied by O(m) [from going through strs] where m is the length of strs
       That would simplify to O(n * log(n))

       Is there a better way to accomplish this?
       '''

       anagrams = defaultdict(list)
       for word in strs:
           anagrams[''.join(sorted(word))].append(word)

       return list(anagrams.values())

    def fasterGroupAnagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        Instead of sorting each word and then storing it in a hashmap, we could count the letters in our word.
        Then the key for our hashmap would be the count of characters rather than the sorted string.
        This would be better because count the letters of a string is O(n) rather than O(n * logn) for sorting that string.

        So, how would we use the count of characters as our hashmap?
        Since we only have to consider a-z, we could make a list of size 26 (one index for each lower case english character).
        We then loop through our word, adding 1 at the proper index in that list (index 0 represent a, index 1 represents b...etc).

        We have to convert our list to a tuple for it to be used as a key
        This means we would end up with a time complexity of O(n * m * 26) = O(n * m)
        '''
        anagrams = defaultdict(list)

        # O(m) where m is the length of strs
        for word in strs:
            # O(26) for list of size 26 creation
            count = [0] * 26

            # O(n) where n is the average length of strings in strs
            for char in word:
                count[ord(char) - ord("a")] += 1

            # O(26) to convert a list of size 26 into a tuple of size 26
            anagrams[tuple(count)].append(word)


        return list(anagrams.values())

solution = Solution()
assert solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], "Test one failed."
assert solution.groupAnagrams( [""]) == [[""]], "Test two failed."
assert solution.groupAnagrams(["a"]) == [["a"]], "Test three failed."

assert solution.fasterGroupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], "Test one failed."
assert solution.fasterGroupAnagrams( [""]) == [[""]], "Test two failed."
assert solution.fasterGroupAnagrams(["a"]) == [["a"]], "Test three failed."
print("All tests passed!")
