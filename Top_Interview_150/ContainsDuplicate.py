"""
Problem: Contains Duplicate

Objective:
- Given an integer array `nums`, return `True` if any value appears at least twice in the array, and `False` if every element is distinct.

Approach:
- The problem can be solved efficiently using a set data structure. By iterating through the list and checking if a number is already in the set, we can detect duplicates in linear time.
- A set is ideal for this problem because it allows for average O(1) time complexity for both insertion and lookup.

Algorithm:
1. **Initialization:**
   - Create an empty set `a` to keep track of the unique numbers encountered in the array.

2. **Iterate Over the Array:**
   - Loop through each number `num` in the array `nums`.
   - For each number, check if it is already present in the set `a`. If it is, that means this number has appeared before, so we return `True` (indicating that a duplicate exists).
   
3. **Add New Elements to the Set:**
   - If the number is not in the set, add it to the set `a`.

4. **Return False:**
   - If the loop completes without finding any duplicates, return `False` (indicating that all elements are distinct).

Time Complexity:
- **Iteration Over List:** O(n), where `n` is the length of the list `nums`. We only iterate through the list once.
- **Set Operations (Insertion and Lookup):** O(1) on average, since set operations like checking for membership and adding elements are typically O(1).
- **Overall Time Complexity:** O(n), which is efficient for this problem.

Space Complexity:
- **Set Storage:** O(n), where `n` is the number of elements in the list, as we store each unique number in the set.
- **Overall Space Complexity:** O(n), required for the set used to track the unique elements.

Edge Cases:
- Empty array: An empty array cannot contain duplicates, so the function will return `False`.
- Array with only one element: A single element array cannot have duplicates, so the function will return `False`.
- Large arrays: The solution will work efficiently even with large arrays, as the time complexity remains linear with respect to the array size.

Example:
Input:
nums = [1, 2, 3, 4, 5]
- All elements are distinct, so no duplicates are found.
Output:
False

Input:
nums = [1, 2, 3, 2, 5]
- The number 2 appears twice, so there is a duplicate.
Output:
True

Code:
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()  
        for num in nums:
            if num in a:  
                return True
            a.add(num)  
        return False  