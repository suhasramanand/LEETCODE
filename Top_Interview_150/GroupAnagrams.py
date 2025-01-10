"""
Problem: Group Anagrams

Objective:
- Given an array of strings `strs`, group the anagrams together and return the groups as a list of lists. 
- Anagrams are words that can be formed by rearranging the letters of another word (e.g., "eat" and "tea" are anagrams).

Approach:
- The problem can be solved by using a hashmap (dictionary) to categorize words by their character frequency.
- For each word in the input array, count the frequency of each character and use this frequency as a key to store words that share the same character counts (i.e., anagrams).

Algorithm:
1. **Frequency Count:**
   - Initialize an empty dictionary `hashmap` to store groups of anagrams.
   - For each word in the input list `strs`, initialize a list `freqCount` of size 26 (for each letter in the alphabet) to store the frequency of each character in the word.
   - Traverse through each character of the word, and for each character, update its corresponding frequency in `freqCount` using `ord(char) - ord('a')`.

2. **Key Representation:**
   - Convert the frequency list `freqCount` into a tuple (since lists can't be used as dictionary keys, but tuples can).
   - This tuple will act as the key for the `hashmap`. Words with the same frequency distribution will have the same key.

3. **Group Anagrams:**
   - Check if the key (tuple) already exists in the `hashmap`.
     - If it does, append the current word to the list associated with that key.
     - If it doesn't, create a new entry in the hashmap with the current word as the first element of the list.

4. **Return the Result:**
   - Once all words are processed, the values of the hashmap will contain the groups of anagrams.
   - Return these values as a list of lists.

Time Complexity:
- **Frequency Count:** O(n * m), where `n` is the number of words and `m` is the average length of each word. We iterate over each word and its characters to compute the frequency count.
- **Overall Complexity:** O(n * m), as dictionary operations (insertion and lookup) are O(1) on average.

Space Complexity:
- **Hashmap Storage:** O(n * m), where `n` is the number of words and `m` is the length of the longest word, as the hashmap stores each word and its frequency count.
- **Overall Space Complexity:** O(n * m), as the storage of anagram groups and frequency counts takes O(n * m) space.

Edge Cases:
- Empty strings: If an empty string is present, it will be grouped with other empty strings.
- All words are distinct: If no words are anagrams of each other, each word will form its own group.
- Identical words: Identical words will be grouped together as anagrams.

Example:
Input:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
- Grouping anagrams:
  - "eat", "tea", "ate" are anagrams.
  - "tan", "nat" are anagrams.
  - "bat" stands alone as it doesn't have any anagrams.
- Output:
  [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Output:
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Code:
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            freqCount = [0]*26
            for char in word:
                freqCount[ord(char) - ord('a')] += 1
            
            key = tuple(freqCount)

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)

        return list(hashmap.values())

        
