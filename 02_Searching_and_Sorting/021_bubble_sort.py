"""
Problem 021: Bubble Sort (with Swapped Flag Optimization)
Phase: 02_Searching_and_Sorting
Difficulty: Easy
Core Concept: Adjacent Comparisons / In-place Swapping / Early Exit Flag / Stability

---
Problem Statement:
Given an array of integers `nums`, sort the array in ascending order using Bubble Sort.
The sorting must be performed IN-PLACE.

Example 1:
    Input: nums = [64, 34, 25, 12, 22, 11, 90]
    Output: [11, 12, 22, 25, 34, 64, 90]

Example 2:
    Input: nums = [5, 1, 4, 2, 8]
    Output: [1, 2, 4, 5, 8]

Example 3 (Already sorted):
    Input: nums = [1, 2, 3, 4, 5]
    Output: [1, 2, 3, 4, 5]
---

Intuition (Air Bubbles Rising to the Surface 🫧):
Think of heavier/larger numbers bubbling up to the end of the array:
1. In pass 1: Compare adjacent pairs `(nums[j], nums[j + 1])`. If `nums[j] > nums[j + 1]`, swap them.
   By the end of pass 1, the LARGEST number is guaranteed to have reached the end (`index n - 1`).
2. In pass 2: The 2nd largest reaches `index n - 2`.
3. In pass `i`: The `i`-th largest settles into its final sorted position.
   So inner loop only needs to run up to `n - 1 - i`!

---
The Critical Optimization: The `swapped` Flag 🚩
Without the flag:
- An already sorted array like `[1, 2, 3, 4, 5]` still executes all O(n^2) comparisons!
With the flag:
- Set `swapped = False` at the start of each outer pass.
- If no swaps occurred during an entire pass (`not swapped`), the array is ALREADY sorted!
- Break immediately!
- Best-case time drops from O(n^2) down to O(n)!

---
Stability:
Bubble Sort is STABLE!
Because we only swap when `nums[j] > nums[j + 1]` (strictly greater), never when equal (`==`).
Elements with identical values preserve their relative original order.

---
Complexity Analysis:
- Best Case Time: O(n) — When array is already sorted (detects no swaps on pass 1).
- Worst Case Time: O(n^2) — When array is reverse sorted.
- Average Case Time: O(n^2).
- Space Complexity: O(1) — Strictly in-place modification.
"""

from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """
    Sorts nums in-place using Bubble Sort with swapped flag optimization.
    
    Args:
        nums (List[int]): Array to be sorted.
        
    Returns:
        List[int]: The sorted array.
    """
    n = len(nums)
    
    for i in range(n - 1):
        swapped = False  # Track if any swap happened in this pass
        
        # Last i elements are already in place
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                # Swap adjacent elements
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                
        # If no two elements were swapped, array is already sorted!
        if not swapped:
            break
            
    return nums


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard unsorted array", [64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ("Already sorted (Best Case O(n))", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("Reverse sorted (Worst Case O(n^2))", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ("Array with duplicates", [4, 2, 4, 1, 3, 2], [1, 2, 2, 3, 4, 4]),
        ("Array with negative numbers", [-5, 10, -20, 0, 3], [-20, -5, 0, 3, 10]),
        ("All identical elements", [7, 7, 7, 7], [7, 7, 7, 7]),
        ("Two elements out of order", [2, 1], [1, 2]),
        ("Single element array", [42], [42]),
        ("Empty array", [], []),
    ]

    print("Running Tests for Problem 021: Bubble Sort\n" + "-" * 70)
    all_passed = True
    for name, original, expected in test_cases:
        arr_copy = list(original)
        actual = bubble_sort(arr_copy)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:34} | Input: {str(original):25} | Sorted: {actual}")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
