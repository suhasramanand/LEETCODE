
/**
 * This class provides a method to remove duplicates from a sorted integer array in-place.
 * The relative order of elements should be preserved, and the array is modified such that
 * the first 'k' elements contain only unique elements.
 * The method returns 'k', the number of unique elements in the array.
 * The remaining elements of the array are not important after the first 'k' unique elements.
 * 
 * Approach:
 * 1. Initialize a pointer 'i' to track the position of the last unique element.
 * 2. Use another pointer 'j' to iterate over the array.
 * 3. If the current element (nums[j]) is different from the last unique element (nums[i]),
 *    increment 'i' and set nums[i] to nums[j] to store the unique element in its correct position.
 * 4. After the iteration, 'i + 1' gives the number of unique elements in the array.
 * 5. Return 'i + 1' as the number of unique elements.
 * 6. The array will have the unique elements in the first 'k' positions and is updated in-place.
 */
package Top_Interview_150;

public class removeDuplicates {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int i = 0;  // Pointer for unique elements
        for (int j = 1; j < nums.length; j++) {  // Pointer for iterating through the array
            if (nums[j] != nums[i]) {  // Found a unique element
                i++;  // Move to the next position
                nums[i] = nums[j];  // Place the unique element in the correct position
            }
        }

        return i + 1;  // Return the number of unique elements
    }

    public static void main(String[] args) {
        removeDuplicates solution = new removeDuplicates();
        
        int[] nums1 = {1, 1, 2};
        int k1 = solution.removeDuplicates(nums1);
        System.out.println("Number of unique elements: " + k1);
        System.out.print("Modified array: ");
        for (int i = 0; i < k1; i++) {
            System.out.print(nums1[i] + " ");
        }
        System.out.println();
        
        int[] nums2 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int k2 = solution.removeDuplicates(nums2);
        System.out.println("Number of unique elements: " + k2);
        System.out.print("Modified array: ");
        for (int i = 0; i < k2; i++) {
            System.out.print(nums2[i] + " ");
        }
        System.out.println();
    }
}

