"""
Problem: Two Sum

Objective:
- Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.
- Each input would have exactly one solution, and you may not use the same element twice.

Approach:
- The problem can be solved efficiently using a hashmap (dictionary). By iterating through the array, we can check if the complement (difference between the target and the current number) exists in the hashmap.
- If it does, we've found the pair of numbers whose sum equals the target, and we return their indices.
- If not, we store the current number and its index in the hashmap for future reference.

Algorithm:
1. **Initialization:**
   - Initialize an empty dictionary `hashmap` to store each number and its index as we iterate through the list.

2. **Iterate Over the List:**
   - For each number `num` at index `i` in `nums`, calculate the difference `diff` between the `target` and the current number (`diff = target - num`).
   
3. **Check for Complement:**
   - If the `diff` (complement) exists in the `hashmap`, it means we've previously encountered a number whose sum with `num` gives the `target`. In this case, return the indices of the complement and the current number: `[hashmap[diff], i]`.

4. **Store the Number and Its Index:**
   - If the complement is not found in the `hashmap`, store the current number `num` and its index `i` in the `hashmap` for future reference.

5. **Return the Result:**
   - Once a valid pair is found, return the indices of the two numbers.
   
Time Complexity:
- **Iteration Over List:** O(n), where `n` is the number of elements in the list `nums`. We only iterate through the list once.
- **Hashmap Operations:** O(1) for insertion and lookup, on average, because dictionary operations in Python are O(1).
- **Overall Time Complexity:** O(n), which is efficient for this problem.

Space Complexity:
- **Hashmap Storage:** O(n), where `n` is the number of elements in `nums`, as the hashmap stores each number and its index.
- **Overall Space Complexity:** O(n), as we store up to `n` elements in the hashmap.

Edge Cases:
- The problem guarantees exactly one solution, so no need to handle cases with no solution.
- The solution assumes the input is valid, i.e., there is always one valid pair, and no index is reused.

Example:
Input:
nums = [2, 7, 11, 15], target = 9
- The difference (target - num) for 2 is 7. Since 7 is found later in the list at index 1, we return the indices of 2 and 7.
Output:
[0, 1]

Input:
nums = [3, 2, 4], target = 6
- The difference (target - num) for 3 is 3, but the number 3 is found at index 0. Then, for 2, the difference is 4, which is found at index 2, so we return the indices of 2 and 4.
Output:
[1, 2]

Code:
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate (nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[num] = i