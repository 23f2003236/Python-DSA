"""
Problem 005: Check if Array is Sorted
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy
Core Concept: Linear Traversal / Invariant Checking / Early Exit

---
Problem Statement:
Given an array (list) of numbers, check whether the array is sorted in non-decreasing
(ascending) order. Return True if it is sorted, otherwise return False.

Example 1:
    Input: nums = [1, 2, 3, 4, 5]
    Output: True

Example 2:
    Input: nums = [5, 4, 3, 2, 1]
    Output: False

Example 3 (Allowing duplicates - Non-decreasing):
    Input: nums = [1, 2, 2, 3, 4]
    Output: True

Example 4 (Empty or single element):
    Input: nums = [42]
    Output: True
---

Intuition (Real-World Analogy: Climbing a Staircase 🪜):
Think of walking up a flight of stairs:
- Every step should either be flat or go higher: `nums[i] <= nums[i + 1]`.
- If at ANY single point you stumble on a step that goes downward (`nums[i] > nums[i + 1]`),
  you immediately know the staircase is NOT ascending!
- You don't need to check the rest of the stairs — stop and return False immediately (Early Exit).
- If you reach the very end without stumbling, the stairs are sorted — return True!

---
Why NOT `nums == sorted(nums)` in an Interview?
- `sorted(nums)` takes O(n log n) time and O(n) extra space.
- Furthermore, it sorts the ENTIRE array even if the very first two elements are out of order!
- A linear scan with early exit takes O(1) best case and O(n) worst case, with O(1) space.

---
Recruiter Bonus Follow-Up 🔥:
"What if the array is sorted and then rotated (e.g., [3, 4, 5, 1, 2])?"
Answer: Count how many times nums[i] > nums[(i + 1) % n].
If this violation happens at most 1 time, the array is a rotated sorted array (LeetCode 1752)!

---
Complexity Analysis:
- Time Complexity: O(n) worst-case (when sorted), O(1) best-case (when nums[0] > nums[1]).
- Space Complexity: O(1) — Constant extra space.
"""

from typing import List


def is_sorted(nums: List[int]) -> bool:
    """
    Checks if a list is sorted in non-decreasing order using a single linear scan.
    
    Args:
        nums (List[int]): List of integers to check.
        
    Returns:
        bool: True if non-decreasing, False otherwise.
    """
    # An empty array or an array with 1 element is always considered sorted
    if len(nums) <= 1:
        return True
    
    # Check adjacent pairs
    for i in range(len(nums) - 1):
        # If any element is strictly greater than its successor, order is violated
        if nums[i] > nums[i + 1]:
            return False  # Early exit
            
    return True


def is_sorted_and_rotated(nums: List[int]) -> bool:
    """
    Recruiter Follow-up: Checks if array was sorted and then rotated.
    e.g., [3, 4, 5, 1, 2] -> True (originally [1, 2, 3, 4, 5])
    """
    if len(nums) <= 1:
        return True
    
    drop_count = 0
    n = len(nums)
    
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            drop_count += 1
            if drop_count > 1:
                return False
                
    return True


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Strictly increasing", [1, 2, 3, 4, 5], True),
        ("With duplicates (non-decreasing)", [1, 2, 2, 3, 4], True),
        ("Strictly decreasing", [5, 4, 3, 2, 1], False),
        ("Unsorted in middle", [1, 3, 2, 4, 5], False),
        ("Unsorted at end", [1, 2, 3, 5, 4], False),
        ("All identical elements", [7, 7, 7, 7], True),
        ("Negative numbers sorted", [-10, -5, -2, 0, 3], True),
        ("Negative numbers unsorted", [-2, -10, 0, 3], False),
        ("Single element", [42], True),
        ("Empty array", [], True),
    ]

    print("Running Tests for Problem 005: Check if Array is Sorted\n" + "-" * 65)
    all_passed = True
    for name, nums, expected in test_cases:
        actual = is_sorted(nums)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:32} | Input: {str(nums):20} | Result: {actual}")
        
    print("-" * 65)
    
    # Follow-up test
    print("\nBonus Recruiter Follow-up: Check Sorted & Rotated")
    rotated_cases = [
        ([3, 4, 5, 1, 2], True),
        ([2, 1, 3, 4], False),
        ([1, 2, 3], True),
    ]
    for nums, expected in rotated_cases:
        actual = is_sorted_and_rotated(nums)
        print(f"Input: {nums} -> Rotated Sorted? {actual} (Expected: {expected})")
        
    print("-" * 65)
    if all_passed:
        print("All test cases passed successfully! ")
