"""
Problem 006: Remove Duplicates from Sorted Array (In-place)
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy (LeetCode 26 - Top Interview Classic)
Core Concept: Two Pointers (Slow & Fast / Reader & Writer) / In-place Array Mutation

---
Problem Statement:
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates
IN-PLACE such that each unique element appears only once. The relative order of the
elements should be kept the same.

Return `k`, the number of unique elements in `nums`.
After your function runs, the first `k` elements of `nums` must contain the unique
elements in their original sorted order. The remaining elements beyond index `k - 1`
do not matter.

Example 1:
    Input: nums = [1, 1, 2]
    Output: k = 2, nums = [1, 2, _]

Example 2:
    Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Output: k = 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]

Example 3:
    Input: nums = []
    Output: 0
---

Intuition (Real-World Analogy: Reader & Writer ✍️📖):
Imagine you are organizing a bookshelf that contains duplicate books placed side-by-side:
1. The first book (`nums[0]`) is always unique. So our `write_ptr` starts at index 0.
2. A fast reader (`read_ptr`) walks from index 1 to the end:
   - If `nums[read_ptr] == nums[write_ptr]`: It's a duplicate! Just ignore it and keep reading.
   - If `nums[read_ptr] != nums[write_ptr]`: A brand-new unique book has been discovered!
     Move `write_ptr` forward by 1, and write this new book there:
     `write_ptr += 1`
     `nums[write_ptr] = nums[read_ptr]`
3. When `read_ptr` finishes scanning, all unique elements are packed neatly into indices
   `0 ... write_ptr`.
4. Total unique elements = `write_ptr + 1`.

---
Beginner Pitfalls & Interview Traps ⚠️:
1. Trap 1: Using `list(set(nums))`
   - Fails in-place requirement! Allocates O(n) auxiliary memory.
   - Python sets do not preserve sorted order.
2. Trap 2: Using `nums.pop(i)` or `del nums[i]` inside a loop
   - In Python lists, deleting from the middle forces all subsequent elements to shift left (O(n)).
   - Doing this in a loop results in terrible O(n^2) time complexity!

---
Complexity Analysis:
- Time Complexity: O(n) — The fast pointer `read_ptr` visits each of the n elements exactly once.
- Space Complexity: O(1) — Strictly in-place modification; only two pointer variables are used.
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Removes duplicates in-place from a sorted array and returns the count of unique items.
    
    Args:
        nums (List[int]): Sorted list of integers.
        
    Returns:
        int: Number of unique elements (k).
    """
    # Edge case: If list is empty, there are 0 unique elements
    if not nums:
        return 0
    
    # write_ptr points to the last known position containing a unique element
    write_ptr = 0
    
    # read_ptr scans through the rest of the array from index 1
    for read_ptr in range(1, len(nums)):
        # When a new unique value is found:
        if nums[read_ptr] != nums[write_ptr]:
            write_ptr += 1
            nums[write_ptr] = nums[read_ptr]  # In-place write
            
    # Total unique elements is write_ptr + 1 (since indices are 0-based)
    return write_ptr + 1


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Multiple duplicates", [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ("Simple duplicates", [1, 1, 2], [1, 2]),
        ("Already all unique", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("All identical elements", [7, 7, 7, 7], [7]),
        ("Negative numbers", [-5, -5, -3, -1, -1, 0, 2], [-5, -3, -1, 0, 2]),
        ("Single element", [42], [42]),
        ("Empty array", [], []),
    ]

    print("Running Tests for Problem 006: Remove Duplicates from Sorted Array\n" + "-" * 70)
    all_passed = True
    for name, original, expected_uniques in test_cases:
        nums_copy = list(original)
        k = remove_duplicates(nums_copy)
        actual_uniques = nums_copy[:k]
        
        passed = (k == len(expected_uniques)) and (actual_uniques == expected_uniques)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:23} | Input: {str(original):25} | k={k}, Unique: {actual_uniques}")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
