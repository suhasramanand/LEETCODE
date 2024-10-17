package Top_Interview_150;
import java.util.Scanner;

public class removeElement {

    // Method to remove all occurrences of val in nums
    public int removeElement(int[] nums, int val) {
        // Pointer for the next position of valid element
        int k = 0;

        // Traverse through all elements in the array
        for (int i = 0; i < nums.length; i++) {
            // If the current element is not equal to val
            if (nums[i] != val) {
                // Place it at the current position of k and increment k
                nums[k] = nums[i];
                k++;
            }
        }
        
        // Return the number of elements that are not equal to val
        return k;
    }

    public static void main(String[] args) {
        // Create a scanner object to take input
        Scanner scanner = new Scanner(System.in);

        // Take array size input
        System.out.println("Enter the size of the array:");
        int size = scanner.nextInt();

        // Declare and initialize the array
        int[] nums = new int[size];

        // Take array elements input
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < size; i++) {
            nums[i] = scanner.nextInt();
        }

        // Take the value to be removed
        System.out.println("Enter the value to be removed:");
        int val = scanner.nextInt();

        // Create an object of removeElement class
        removeElement solution = new removeElement();

        // Call the removeElement method and get the result
        int k = solution.removeElement(nums, val);


        System.out.println("Number of elements not equal to " + val + ": " + k);
        System.out.println("The modified array is:");
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}