"""
Problem 002: Find Minimum Element in an Array
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy
Core Concept: Linear Traversal / Invariant Maintenance

---
Problem Statement:
Given an array (list) of numbers, find and return the minimum (smallest) element.

Example 1:
    Input: nums = [3, 5, 1, 9, 2]
    Output: 1

Example 2:
    Input: nums = [-10, -3, -50, -1]
    Output: -50

Example 3:
    Input: nums = [42]
    Output: 42
---

Intuition (Real-World Analogy):
Looking for the shortest person in a line:
1. Assume the very first person in line is the shortest so far (`current_min = nums[0]`).
2. Walk down the line, inspecting one person at a time.
3. If you see someone shorter than your `current_min`, update `current_min`.
4. At the end of the line, `current_min` is guaranteed to be the shortest.

---
Beginner Pitfall Alert ⚠️:
Never initialize `min_val = 0`!
Why? If all numbers in the array are positive (e.g., `[10, 20, 30]`), your function
would return `0`, which is not even present in the input!
Always initialize with:
- The first element: `nums[0]` (after verifying non-empty), OR
- Positive infinity: `float('inf')`.

---
Complexity Analysis:
- Time Complexity: O(n) — We traverse the list of n elements exactly once.
- Space Complexity: O(1) — We only store a single variable `current_min`.
"""

from typing import List, Optional


def find_minimum(nums: List[int]) -> Optional[int]:
    """
    Finds the minimum value in a list of integers using a single-pass linear scan.
    
    Args:
        nums (List[int]): List of integers.
        
    Returns:
        Optional[int]: The minimum integer, or None if the list is empty.
    """
    # Edge Case: Check for empty input list
    if not nums:
        return None
    
    # Invariant: current_min stores the minimum value seen in nums[0...i]
    current_min = nums[0]
    
    # Iterate through the remaining elements starting from index 1
    for num in nums[1:]:
        if num < current_min:
            current_min = num
            
    return current_min


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Positive numbers", [3, 5, 1, 9, 2], 1),
        ("All negative numbers", [-10, -3, -50, -1], -50),
        ("Single element", [42], 42),
        ("Duplicates / All same", [7, 7, 7, 7], 7),
        ("Already sorted ascending", [1, 2, 3, 4, 5], 1),
        ("Sorted descending", [5, 4, 3, 2, 1], 1),
        ("Empty list", [], None),
    ]

    print("Running Tests for Problem 002: Find Minimum Element\n" + "-" * 55)
    all_passed = True
    for name, nums, expected in test_cases:
        actual = find_minimum(nums)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:26} | Input: {str(nums):20} | Result: {actual} (Expected: {expected})")
        
    print("-" * 55)
    if all_passed:
        print("All test cases passed successfully!")
