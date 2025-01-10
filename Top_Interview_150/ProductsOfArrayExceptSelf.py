"""
Problem: Products of Array Except Self

Objective:
- Given an integer array `nums`, return an array `output` where `output[i]` is the product of 
  all elements in `nums` except `nums[i]`.
- Solve in O(n) time without using division.

Approach:
1. **Prefix and Suffix Products**:
   - For each index `i`, the product of all elements except `nums[i]` can be computed as:
     output[i] = product of all elements to the left of `i` (prefix) 
                 × product of all elements to the right of `i` (suffix).
   - By precomputing prefix and suffix products, we can calculate the output efficiently.

2. **Optimization (Single Pass)**:
   - Instead of maintaining separate arrays for prefix and suffix products, we can calculate 
     and store these products in the `output` array directly using two passes:
       - First pass: Compute and store prefix products in the `output` array.
       - Second pass: Traverse from the end of the array to calculate suffix products, 
         multiplying them with the prefix values already in the `output` array.

Algorithm:
1. Initialize the `output` array with all elements as 1.
2. Compute prefix products in the first pass:
   - Traverse the array from left to right.
   - Store the cumulative product of elements before the current index in `output[i]`.
3. Compute suffix products in the second pass:
   - Traverse the array from right to left.
   - Multiply the cumulative product of elements after the current index with the value in `output[i]`.
4. Return the `output` array.

Example Walkthrough:
Input: nums = [1, 2, 4, 6]
- Step 1: Compute Prefix Products:
  output = [1, 1, 2, 8]
- Step 2: Compute Suffix Products:
  output = [48, 24, 12, 8]

Edge Cases:
- Array contains zeros: nums = [0, 1, 2] → output = [2, 0, 0]
- All elements are the same: nums = [1, 1, 1] → output = [1, 1, 1]
- Minimum length array: nums = [1, 2] → output = [2, 1]

Complexity Analysis:
- Time Complexity: O(n) (Two passes over the array)
- Space Complexity: O(1) (In-place computation, ignoring the output array)

Code:
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        output = [1]*n

        prefix_product = 1
        for i in range(n):
            output[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(n-1, -1, -1):
            output [i] *= suffix_product
            suffix_product *= nums[i]

        return output
