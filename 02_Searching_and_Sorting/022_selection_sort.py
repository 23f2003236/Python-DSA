"""
Problem 022: Selection Sort
Phase: 02_Searching_and_Sorting
Difficulty: Easy
Core Concept: Minimum Selection Invariant / In-place Array Partitioning / Minimum Swaps

---
Problem Statement:
Given an array of integers `nums`, sort the array in ascending order using Selection Sort.
The sorting must be performed IN-PLACE.

Example 1:
    Input: nums = [64, 25, 12, 22, 11]
    Output: [11, 12, 22, 25, 64]

Example 2:
    Input: nums = [5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5]

Example 3:
    Input: nums = [1, 2, 3]
    Output: [1, 2, 3]
---

Intuition (Selecting the Smallest Person in Line 🧍‍♂️):
Divide the array conceptually into two segments:
1. Left side: Sorted prefix (`0 ... i - 1`)
2. Right side: Unsorted suffix (`i ... n - 1`)

Algorithm:
In each pass `i` (from 0 to n - 2):
1. Assume the element at index `i` is the minimum (`min_idx = i`).
2. Scan through the remaining unsorted suffix (`j = i + 1 to n - 1`):
   If `nums[j] < nums[min_idx]`, update `min_idx = j`.
3. After finding the minimum element in the suffix, swap `nums[i]` with `nums[min_idx]`!
4. The sorted prefix has now expanded by 1 element!

---
Key Interview Insights & Questions:

1. When is Selection Sort preferred over Bubble Sort?
   👉 Selection Sort makes the MINIMUM number of swaps!
   It performs at most `n - 1` swaps total (O(n) writes).
   If memory writes are very expensive (e.g. writing to EEPROM/Flash memory),
   Selection Sort is advantageous because it minimizes write operations.

2. Is Selection Sort Stable?
   ❌ NO, Selection Sort is UNSTABLE!
   Example: [4a, 4b, 2]
   - Step 1: Minimum is 2. Swap 4a with 2 -> [2, 4b, 4a].
   - Notice that 4a was originally before 4b, but ended up after 4b!
   - Long-distance swaps destroy the relative order of identical keys.

3. Time Complexity:
   Unlike Bubble Sort, Selection Sort's best-case time is STILL O(n^2)!
   Even if the array is already sorted, it must still scan the entire remaining suffix
   to confirm that `nums[i]` is indeed the minimum.

---
Complexity Analysis:
- Best Case Time: O(n^2)
- Worst Case Time: O(n^2)
- Average Case Time: O(n^2)
- Space Complexity: O(1) — In-place.
- Total Swaps: At most n - 1 (O(n) writes).
"""

from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    """
    Sorts nums in-place using Selection Sort.
    
    Args:
        nums (List[int]): Array to be sorted.
        
    Returns:
        List[int]: The sorted array.
    """
    n = len(nums)
    
    for i in range(n - 1):
        min_idx = i  # Assume current position holds the minimum
        
        # Search for the true minimum in the unsorted suffix [i + 1 ... n - 1]
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the element at index i
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            
    return nums


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard unsorted array", [64, 25, 12, 22, 11], [11, 12, 22, 25, 64]),
        ("Reverse sorted array", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ("Already sorted array", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("Array with duplicates", [4, 2, 4, 1, 3, 2], [1, 2, 2, 3, 4, 4]),
        ("Array with negative numbers", [-10, 5, -20, 0, 3], [-20, -10, 0, 3, 5]),
        ("All identical elements", [7, 7, 7, 7], [7, 7, 7, 7]),
        ("Two elements out of order", [2, 1], [1, 2]),
        ("Single element array", [42], [42]),
        ("Empty array", [], []),
    ]

    print("Running Tests for Problem 022: Selection Sort\n" + "-" * 70)
    all_passed = True
    for name, original, expected in test_cases:
        arr_copy = list(original)
        actual = selection_sort(arr_copy)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:32} | Input: {str(original):22} | Sorted: {actual}")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
