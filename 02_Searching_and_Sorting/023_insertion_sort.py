"""
Problem 023: Insertion Sort (The Card Player's Shifting Algorithm)
Phase: 02_Searching_and_Sorting
Difficulty: Easy
Core Concept: Incremental Sorting / In-place Shifting / Adaptive Behavior / Timsort Foundation

---
Problem Statement:
Given an array of integers `nums`, sort the array in ascending order using Insertion Sort.
The sorting must be performed IN-PLACE.

Example 1:
    Input: nums = [12, 11, 13, 5, 6]
    Output: [5, 6, 11, 12, 13]

Example 2:
    Input: nums = [5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5]

Example 3:
    Input: nums = [1, 2, 3, 4]
    Output: [1, 2, 3, 4]
---

Intuition (Sorting Playing Cards in Hand 🃏):
Imagine holding playing cards in your hand:
1. The first card (`nums[0]`) is trivially already sorted.
2. Pick up the next card: `key = nums[i]`.
3. Compare `key` with cards to its left (`j = i - 1, i - 2, ...`):
   - As long as `nums[j] > key`, shift `nums[j]` one spot to the right (`nums[j + 1] = nums[j]`).
4. Once you find a card `<= key` (or hit the left boundary), place `key` into the empty slot:
   `nums[j + 1] = key`.
5. Repeat for all elements from index 1 to n - 1!

---
Recruiter Level Insights 🔥:

1. Why is Insertion Sort used in Python's built-in `sort()` (Timsort)?
   Python's `list.sort()` uses Timsort (a hybrid of Merge Sort + Insertion Sort).
   For small subarrays (size <= 32 or 64), Insertion Sort has virtually zero function-call
   overhead, exceptional CPU cache locality, and very fast execution!

2. Adaptive Nature (Best Case O(n)):
   If an array is already sorted, the inner while-loop condition `nums[j] > key`
   fails on the very first check!
   Total time = O(n) with 0 shifts.

3. Stability:
   Insertion Sort is STABLE!
   Identical keys are never shifted past each other because the condition is strictly
   `nums[j] > key` (not `>=`).

---
Complexity Analysis:
- Best Case Time: O(n) — When array is already sorted or nearly sorted.
- Worst Case Time: O(n^2) — When array is reverse sorted.
- Average Case Time: O(n^2).
- Space Complexity: O(1) — Strictly in-place modification.
"""

from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    """
    Sorts nums in-place using Insertion Sort.
    
    Args:
        nums (List[int]): Array to be sorted.
        
    Returns:
        List[int]: The sorted array.
    """
    n = len(nums)
    
    # Iterate from the 2nd element to the end
    for i in range(1, n):
        key = nums[i]  # The card to insert into the sorted left portion
        j = i - 1
        
        # Shift elements of nums[0...i-1] that are greater than key to one position ahead
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # Shift right
            j -= 1
            
        # Place key in its correct sorted position
        nums[j + 1] = key
        
    return nums


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard unsorted array", [12, 11, 13, 5, 6], [5, 6, 11, 12, 13]),
        ("Reverse sorted array", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ("Already sorted array", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("Nearly sorted array", [1, 2, 4, 3, 5], [1, 2, 3, 4, 5]),
        ("Array with duplicates", [4, 2, 4, 1, 3, 2], [1, 2, 2, 3, 4, 4]),
        ("Negative numbers", [-5, 10, -20, 0, 3], [-20, -5, 0, 3, 10]),
        ("All identical elements", [7, 7, 7, 7], [7, 7, 7, 7]),
        ("Single element array", [42], [42]),
        ("Empty array", [], []),
    ]

    print("Running Tests for Problem 023: Insertion Sort\n" + "-" * 70)
    all_passed = True
    for name, original, expected in test_cases:
        arr_copy = list(original)
        actual = insertion_sort(arr_copy)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:32} | Input: {str(original):22} | Sorted: {actual}")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
