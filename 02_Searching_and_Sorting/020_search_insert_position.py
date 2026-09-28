"""
Problem 020: Search Insert Position
Phase: 02_Searching_and_Sorting
Difficulty: Easy (LeetCode 35 - Top Interview Classic)
Core Concept: Binary Search Boundary Invariant / Insertion Position

---
Problem Statement:
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1, 3, 5, 6], target = 5
    Output: 2

Example 2:
    Input: nums = [1, 3, 5, 6], target = 2
    Output: 1 (2 should be inserted between 1 and 3)

Example 3:
    Input: nums = [1, 3, 5, 6], target = 7
    Output: 4 (7 should be inserted at the end)

Example 4:
    Input: nums = [1, 3, 5, 6], target = 0
    Output: 0 (0 should be inserted at the beginning)
---

Intuition (The Golden Invariant of `low` 🌟):
Run standard Binary Search:
    low = 0, high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

What happens when the target is NOT found and the loop terminates?
When the loop ends, `low` has crossed `high` (`low = high + 1`).
At this exact moment:
- All elements at indices < `low` are strictly SMALLER than `target`.
- All elements at indices >= `low` are strictly GREATER than `target`.
Therefore, `low` is mathematically the EXACT index where `target` belongs!
Simply `return low`!

---
Relationship to Python's `bisect`:
`return low` behaves exactly like `bisect.bisect_left(nums, target)`!

---
Complexity Analysis:
- Time Complexity: O(log n) — Binary search halving the search space each step.
- Space Complexity: O(1) — Constant memory.
"""

from typing import List
import bisect


def search_insert(nums: List[int], target: int) -> int:
    """
    Finds the index of target or where it should be inserted using binary search.
    
    Args:
        nums (List[int]): Sorted list of distinct integers.
        target (int): Target value to search or insert.
        
    Returns:
        int: Index of target or insertion point.
    """
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    # When target is not found, low points to the correct insertion index!
    return low


def search_insert_bisect(nums: List[int], target: int) -> int:
    """
    Equivalent standard library implementation.
    """
    return bisect.bisect_left(nums, target)


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Target present in middle", [1, 3, 5, 6], 5, 2),
        ("Target absent in middle", [1, 3, 5, 6], 2, 1),
        ("Target larger than all elements", [1, 3, 5, 6], 7, 4),
        ("Target smaller than all elements", [1, 3, 5, 6], 0, 0),
        ("Target present at beginning", [10, 20, 30], 10, 0),
        ("Target present at end", [10, 20, 30], 30, 2),
        ("Single element found", [42], 42, 0),
        ("Single element insert before", [42], 10, 0),
        ("Single element insert after", [42], 99, 1),
        ("Empty array insert", [], 5, 0),
    ]

    print("Running Tests for Problem 020: Search Insert Position\n" + "-" * 75)
    all_passed = True
    for name, nums, target, expected in test_cases:
        res_custom = search_insert(nums, target)
        res_bisect = search_insert_bisect(nums, target)
        
        passed = (res_custom == expected) and (res_bisect == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:34} | Target: {str(target):2} | Insert Index: {res_custom:2} (Expected: {expected})")
        
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! Day 5 Complete (20/100)!")
