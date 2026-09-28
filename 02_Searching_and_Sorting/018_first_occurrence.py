"""
Problem 018: First Occurrence of an Element (Modified Binary Search)
Phase: 02_Searching_and_Sorting
Difficulty: Easy-Medium (Classic Interview Pattern / bisect_left Foundation)
Core Concept: Binary Search with Leftward Bias / Candidate Tracking

---
Problem Statement:
Given a sorted array of integers `nums` (which may contain duplicate values)
and an integer `target`, find the index of the FIRST (leftmost) occurrence of `target`.
If `target` does not exist in `nums`, return -1.

Example 1:
    Input: nums = [2, 4, 4, 4, 6, 7], target = 4
    Output: 1
    Explanation: The number 4 appears at indices 1, 2, and 3. The first occurrence is at index 1.

Example 2:
    Input: nums = [5, 7, 7, 8, 8, 10], target = 8
    Output: 3

Example 3:
    Input: nums = [1, 2, 3, 5], target = 4
    Output: -1
---

Intuition (The "Don't Stop at the First Match" Mindset 🛑➡️⬅️):
In standard Binary Search (Problem 017):
- The instant `nums[mid] == target`, you stop and return `mid`.
- But if the array has DUPLICATES, `mid` might be in the middle or end of the duplicate cluster!

To find the FIRST occurrence:
1. When `nums[mid] == target`:
   - Don't stop!
   - Save `result = mid` (this is our current best candidate).
   - An earlier occurrence can only exist to the LEFT!
   - Shrink search space leftward: `high = mid - 1`.
2. When `nums[mid] < target`:
   - Target is strictly to the right: `low = mid + 1`.
3. When `nums[mid] > target`:
   - Target is strictly to the left: `high = mid - 1`.
4. When the loop terminates (`low > high`), `result` holds the exact first occurrence index!

---
Relationship to Python's `bisect_left`:
This exact logic powers `bisect.bisect_left(nums, target)` in Python's standard library.
Understanding this manual implementation is crucial for solving harder problems like
LeetCode 34 ("Find First and Last Position of Element in Sorted Array").

---
Complexity Analysis:
- Time Complexity: O(log n) — The search space is strictly halved each step.
- Space Complexity: O(1) — Uses constant extra space.
"""

from typing import List
import bisect


def find_first_occurrence(nums: List[int], target: int) -> int:
    """
    Finds the index of the first occurrence of target using modified binary search.
    
    Args:
        nums (List[int]): Sorted list of integers (may contain duplicates).
        target (int): Value to search for.
        
    Returns:
        int: Index of first occurrence, or -1 if not found.
    """
    low = 0
    high = len(nums) - 1
    first_index = -1  # Default if target is not found
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            first_index = mid  # Record candidate
            high = mid - 1     # Continue searching in left half for earlier occurrence
        elif nums[mid] < target:
            low = mid + 1      # Target is to the right
        else:
            high = mid - 1     # Target is to the left
            
    return first_index


def find_first_occurrence_bisect(nums: List[int], target: int) -> int:
    """
    Standard library approach using bisect_left for comparison.
    """
    idx = bisect.bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    return -1


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Multiple duplicates in middle", [2, 4, 4, 4, 6, 7], 4, 1),
        ("Duplicates at start of array", [1, 1, 1, 2, 3], 1, 0),
        ("Duplicates at end of array", [1, 2, 3, 5, 5, 5], 5, 3),
        ("All elements are identical target", [7, 7, 7, 7, 7], 7, 0),
        ("Single target occurrence", [1, 3, 5, 7, 9], 5, 2),
        ("Target not present (in between)", [1, 2, 4, 5], 3, -1),
        ("Target smaller than all elements", [10, 20, 30], 5, -1),
        ("Target larger than all elements", [10, 20, 30], 40, -1),
        ("Single element found", [42], 42, 0),
        ("Single element not found", [42], 99, -1),
        ("Empty list", [], 5, -1),
    ]

    print("Running Tests for Problem 018: First Occurrence of an Element\n" + "-" * 75)
    all_passed = True
    for name, nums, target, expected in test_cases:
        res_custom = find_first_occurrence(nums, target)
        res_bisect = find_first_occurrence_bisect(nums, target)
        
        passed = (res_custom == expected) and (res_bisect == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:34} | Target: {str(target):2} | Custom: {res_custom:2} | Bisect: {res_bisect:2} (Exp: {expected})")
        
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! ")
