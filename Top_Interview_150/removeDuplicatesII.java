/**
 * This class provides a method to remove duplicates from a sorted integer array in-place,
 * allowing each unique element to appear at most twice.
 * 
 * Approach:
 * 1. Use a pointer `i` to track the position where the next valid element should be placed.
 * 2. Iterate through the array with another pointer `j`.
 * 3. If the current element `nums[j]` can appear (i.e., it's either the first element or appears at most twice),
 *    place it at `nums[i]` and increment `i`.
 * 4. After iteration, the first `i` elements in `nums` will contain the desired result.
 * 5. Return `i` as the count of elements in the modified array.
 */
package Top_Interview_150;

public class removeDuplicatesII {

    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        
        int i = 1;
        int count = 1;
        
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] == nums[j - 1]) {
                count++;
            } else {
                count = 1; 
            }

            if (count <= 2) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }

    public static void main(String[] args) {
        removeDuplicatesII solution = new removeDuplicatesII();
        
        int[] nums1 = {1, 1, 1, 2, 2, 3};
        int k1 = solution.removeDuplicates(nums1);
        System.out.println("Number of unique elements (with at most two occurrences): " + k1);
        System.out.print("Modified array: ");
        for (int i = 0; i < k1; i++) {
            System.out.print(nums1[i] + " ");
        }
        System.out.println();
        
        int[] nums2 = {0, 0, 1, 1, 1, 1, 2, 3, 3};
        int k2 = solution.removeDuplicates(nums2);
        System.out.println("Number of unique elements (with at most two occurrences): " + k2);
        System.out.print("Modified array: ");
        for (int i = 0; i < k2; i++) {
            System.out.print(nums2[i] + " ");
        }
        System.out.println();
    }
}
