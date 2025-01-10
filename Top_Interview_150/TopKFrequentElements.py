"""
Problem: Top K Frequent Elements

Objective:
- Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in the array.

Approach:
- The task can be solved by counting the frequency of each element in the array, sorting these elements by frequency, and returning the top `k` frequent ones.
- Use a dictionary to store the frequency of each element.
- Sort the dictionary entries by frequency and select the top `k` elements.

Algorithm:
1. **Count Frequencies:**
   - Initialize an empty dictionary `count` to store the frequency of each element in `nums`.
   - Iterate through the array `nums`, for each element `num`, increment its count in the dictionary.

2. **Sort Elements by Frequency:**
   - Create an empty list `arr` where each element will be a tuple `[frequency, element]`.
   - Iterate over the `count` dictionary and append each `[frequency, element]` pair to `arr`.

3. **Sort the List:**
   - Sort the `arr` list based on the frequency (first item of the tuple). By default, Python sorts in ascending order, so the list will be sorted from the least frequent to the most frequent elements.

4. **Extract the Top K Elements:**
   - Initialize an empty list `res` to store the result.
   - Pop the last element (most frequent) from `arr` until the list contains `k` elements.
   - Append the element (second item of the tuple) to the result list `res`.

5. **Return the Result:**
   - Return the list `res` containing the top `k` frequent elements.

Time Complexity:
- **Counting Frequencies:** O(n), where `n` is the length of the input array. We iterate over the array once to count frequencies.
- **Sorting the Elements:** O(m log m), where `m` is the number of unique elements in `nums`. Sorting the list of unique elements will take `m log m` time.
- **Overall Complexity:** O(n + m log m), which is efficient enough given the problem constraints.

Space Complexity:
- **Frequency Dictionary:** O(m), where `m` is the number of unique elements.
- **List for Sorted Elements:** O(m), as we store all unique elements in the sorted list.
- **Overall Space Complexity:** O(m), where `m` is the number of unique elements in the input array.

Edge Cases:
- If `k` is equal to the length of the array, all elements in the array will be returned.
- If there are multiple elements with the same frequency, the order of those elements in the result list may not be the same as in the original array.

Example:
Input:
nums = [1,1,1,2,2,3], k = 2
- Frequency count: {1: 3, 2: 2, 3: 1}
- Sorted by frequency: [(3, 1), (2, 2), (1, 3)]
- Top 2 frequent elements: [1, 2]

Output:
[1, 2]

Code:
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res