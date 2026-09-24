"""
Problem 001: Find Maximum Element in an Array
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy
Core Concept: Linear Traversal / Invariant Maintenance

---
Problem Statement:
Given an array (list) of numbers, find and return the maximum element.

Example 1:
    Input: nums = [3, 5, 1, 9, 2]
    Output: 9

Example 2:
    Input: nums = [-10, -3, -50, -1]
    Output: -1

Example 3:
    Input: nums = [42]
    Output: 42
---

Intuition (Real-World Analogy):
Imagine you are a teacher looking for the tallest student in a classroom line.
1. You assume the very first student in line is the tallest so far (`current_max = nums[0]`).
2. You walk down the line, inspecting one student at a time.
3. If you see someone taller than your `current_max`, you update `current_max`.
4. By the time you reach the end of the line, `current_max` is guaranteed to be the tallest.

---
Beginner Pitfall Alert ⚠️:
Never initialize `max_val = 0`!
Why? If all numbers in the array are negative (e.g., `[-10, -5, -20]`), your function
would return `0`, which isn't even in the array!
Always initialize with either:
- The first element: `nums[0]` (after verifying the list is non-empty), OR
- Negative infinity: `float('-inf')`.

---
Complexity Analysis:
- Time Complexity: O(n) — We traverse the list of n elements exactly once.
- Space Complexity: O(1) — We only store a single variable `current_max`.
"""

from typing import List, Optional


def find_maximum(nums: List[int]) -> Optional[int]:
    """
    Finds the maximum value in a list of integers using a single-pass linear scan.
    
    Args:
        nums (List[int]): List of integers.
        
    Returns:
        Optional[int]: The maximum integer, or None if the list is empty.
    """
    # Edge Case: Check for empty input list
    if not nums:
        return None
    
    # Invariant: current_max stores the maximum value seen in nums[0...i]
    current_max = nums[0]
    
    # Iterate through the remaining elements starting from index 1
    for num in nums[1:]:
        if num > current_max:
            current_max = num
            
    return current_max


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Positive numbers", [3, 5, 1, 9, 2], 9),
        ("All negative numbers", [-10, -3, -50, -1], -1),
        ("Single element", [42], 42),
        ("Duplicates / All same", [7, 7, 7, 7], 7),
        ("Already sorted ascending", [1, 2, 3, 4, 5], 5),
        ("Sorted descending", [5, 4, 3, 2, 1], 5),
        ("Empty list", [], None),
    ]

    print("Running Tests for Problem 001: Find Maximum Element\n" + "-" * 55)
    all_passed = True
    for name, nums, expected in test_cases:
        actual = find_maximum(nums)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:26} | Input: {str(nums):20} | Result: {actual} (Expected: {expected})")
        
    print("-" * 55)
    if all_passed:
        print("All test cases passed successfully! ")
