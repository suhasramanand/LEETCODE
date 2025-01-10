"""
Problem: Design an Encoding and Decoding Scheme for Strings

Objective:
- You are given a list of strings `strs`. Your task is to implement an encoding and decoding scheme.
- Encode: Convert the list of strings into a single string.
- Decode: Convert the encoded string back into the original list of strings.

Approach:
- The encoding and decoding process can be achieved by representing each string with its length and content in a special format.
- For each string, append its length followed by a separator (e.g., `#`), and then append the string itself.
- To decode, extract the length of each string and use that information to recover the original strings.

Encoding:
- For each string `s` in the input list:
  - Compute the length of the string.
  - Combine the length, separator (`#`), and the string itself into a single encoded segment: `"length#string"`.
  - Concatenate all such segments to form the encoded result.

Decoding:
- Iterate through the encoded string:
  - Extract the length of the next string (by reading until the separator `#`).
  - Extract the string content using the extracted length and append it to the result.
  - Repeat until the entire encoded string is processed.

Algorithm:
1. **Encoding:**
   - Initialize an empty string `res`.
   - For each string `s` in the input list:
     - Append the string's length, a separator (`#`), and the string itself to `res`.
   - Return the resulting encoded string `res`.
   
2. **Decoding:**
   - Initialize an empty list `res` to store the decoded strings.
   - Use a pointer `i` to traverse the encoded string:
     - Find the position of the separator (`#`) to determine the length of the next string.
     - Extract the string from the encoded string using the length.
     - Move the pointer forward by the length of the string plus the separator and the length itself.
   - Continue the process until all strings are decoded.

Time Complexity:
- **Encoding:** O(n), where n is the total number of characters in all strings. We traverse the list of strings once and append the corresponding encoded parts.
- **Decoding:** O(n), where n is the length of the encoded string. We process each character of the encoded string once.

Space Complexity:
- **Encoding:** O(n), where n is the total length of the encoded string.
- **Decoding:** O(n), where n is the number of characters in the decoded strings.

Edge Cases:
- Empty string: "" will be encoded as "0#". When decoded, it will result in an empty string.
- Strings with special characters: They are handled as part of the string content and encoded in the same way as regular strings.

Example:
Input:
strs = ["hello", "world"]
Encoding process:
- "hello" becomes "5#hello"
- "world" becomes "5#world"
Encoded result: "5#hello5#world"
Decoding process:
- "5#hello" → length = 5, string = "hello"
- "5#world" → length = 5, string = "world"
Decoded result: ["hello", "world"]

Code:
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [],0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1+length
        return res
