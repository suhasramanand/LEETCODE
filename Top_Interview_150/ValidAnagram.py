"""
Problem: Valid Anagram

Objective:
- Given two strings `s` and `t`, determine if `t` is an anagram of `s`. 
- An anagram of a string is another string that contains the same characters, only the order of the characters can be different.

Approach:
- The problem can be solved by comparing the frequency of each character in both strings. If both strings have identical character counts for every character, then one is an anagram of the other.
- The solution uses a dictionary (`count`) to keep track of the frequency of each character in `s`, and then subtracts the frequency of characters found in `t`. If all values in the dictionary are zero after processing both strings, then the strings are anagrams.

Algorithm:
1. **Check Lengths:**
   - First, compare the lengths of the two strings. If the lengths differ, they cannot be anagrams, so return `False` immediately.

2. **Count Characters in `s`:**
   - Initialize an empty dictionary `count` to store the frequency of characters in string `s`.
   - Loop through each character `char` in string `s`. For each character, increase its count in the dictionary.

3. **Subtract Counts Based on `t`:**
   - Loop through each character `char` in string `t`. For each character, decrease its count in the dictionary.
   - If a character in `t` is not present in `s`, its count will remain negative. This can also be used as an early exit condition if you prefer to stop early when an invalid character is found.

4. **Final Check:**
   - After processing both strings, loop through the values in the `count` dictionary. If any value is not zero, it means the characters in `s` and `t` were not the same, so return `False`.
   - If all values are zero, the strings are anagrams, so return `True`.

Time Complexity:
- **Character Counting:** O(n), where `n` is the length of the strings `s` and `t` (since they have equal length). We loop through each string once.
- **Final Check:** O(1) for checking all character counts (as there are at most 26 different characters in the alphabet).
- **Overall Time Complexity:** O(n), which is efficient for this problem.

Space Complexity:
- **Dictionary Storage:** O(n), where `n` is the number of characters in the strings, as the dictionary stores the frequency of each character.
- **Overall Space Complexity:** O(n), which is required for storing the frequency of characters.

Edge Cases:
- Strings of different lengths: If `s` and `t` have different lengths, they cannot be anagrams, and the function returns `False`.
- Empty strings: Two empty strings are trivially anagrams of each other.
- Strings with the same characters but different frequencies: The strings will not be anagrams if the frequencies of the characters differ.

Example:
Input:
s = "anagram", t = "nagaram"
- Both strings contain the same characters with the same frequency, so they are anagrams.
Output:
True

Input:
s = "rat", t = "car"
- The strings contain different characters, so they are not anagrams.
Output:
False

Code:
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char,0) + 1
        for char in t:
            count[char] = count.get(char,0) - 1

        for value in count.values():
            if value != 0:
                return False
        return True
    
        