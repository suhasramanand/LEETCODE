package Top_Interview_150;

import java.util.Scanner;

public class mergeSortArray {

    // Function to merge nums2 into nums1
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1; //Pointer for the last element of nums1's actual values
        int j = n - 1; // Pointer for the last element of nums2
        int k = m + n - 1; // PPointer for the last position in nums1

        // Start from the end of both arrays and place the largest element in nums1
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--]; 
            } else {
                nums1[k--] = nums2[j--]; 
            }
        }

        // If there are remaining elements in nums2, copy them into nums1
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }

    // Main method - the entry point of the program
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Taking input for nums1
        System.out.print("Enter the number of elements in nums1 (m): ");
        int m = scanner.nextInt();

        int[] nums1 = new int[m + 100]; // Allocating extra space for the merge (can adjust this)
        System.out.print("Enter the elements of nums1: ");
        for (int i = 0; i < m; i++) {
            nums1[i] = scanner.nextInt();
        }

        // Taking input for nums2
        System.out.print("Enter the number of elements in nums2 (n): ");
        int n = scanner.nextInt();

        int[] nums2 = new int[n];
        System.out.print("Enter the elements of nums2: ");
        for (int i = 0; i < n; i++) {
            nums2[i] = scanner.nextInt();
        }

        // Merging nums2 into nums1
        merge(nums1, m, nums2, n);

        // Output the result
        System.out.println("Merged array:");
        for (int i = 0; i < m + n; i++) {
            System.out.print(nums1[i] + " ");
        }

        scanner.close();
    }
    
}
