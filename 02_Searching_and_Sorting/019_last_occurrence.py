"""
Problem 019: Last Occurrence of an Element (Modified Binary Search)
Phase: 02_Searching_and_Sorting
Difficulty: Easy-Medium (Classic Interview Pattern / bisect_right Foundation)
Core Concept: Binary Search with Rightward Bias / Range Finding (LeetCode 34)

---
Problem Statement:
Given a sorted array of integers `nums` (which may contain duplicate values)
and an integer `target`, find the index of the LAST (rightmost) occurrence of `target`.
If `target` does not exist in `nums`, return -1.

Example 1:
    Input: nums = [2, 4, 4, 4, 6, 7], target = 4
    Output: 3
    Explanation: The number 4 appears at indices 1, 2, and 3. The last occurrence is at index 3.

Example 2:
    Input: nums = [5, 7, 7, 8, 8, 10], target = 8
    Output: 4

Example 3:
    Input: nums = [1, 2, 3, 5], target = 4
    Output: -1
---

Intuition (Rightward Bias Mindset ➡️):
In Problem 018 (First Occurrence), upon finding `nums[mid] == target`, we searched LEFT.
To find the LAST occurrence:
1. When `nums[mid] == target`:
   - Don't stop!
   - Save `last_index = mid` (this is our current best candidate).
   - A later occurrence can only exist to the RIGHT!
   - Shrink search space rightward: `low = mid + 1`.
2. When `nums[mid] < target`:
   - Target is strictly to the right: `low = mid + 1`.
3. When `nums[mid] > target`:
   - Target is strictly to the left: `high = mid - 1`.
4. When the loop terminates, `last_index` holds the exact last occurrence index!

---
Recruiter Connection: LeetCode 34 (First and Last Position of Element):
By combining:
- `first = find_first_occurrence(nums, target)` (Problem 018)
- `last = find_last_occurrence(nums, target)` (Problem 019)
You completely solve LeetCode 34 in O(log n) time and O(1) space!
Also: Total count of target occurrences in a sorted array is simply:
`count = (last - first + 1)` if first != -1 else 0!

---
Complexity Analysis:
- Time Complexity: O(log n) — Binary search strictly halves the search space.
- Space Complexity: O(1) — Constant auxiliary memory.
"""

from typing import List, Tuple
import bisect


def find_last_occurrence(nums: List[int], target: int) -> int:
    """
    Finds the index of the last occurrence of target using binary search with rightward bias.
    
    Args:
        nums (List[int]): Sorted list of integers (may contain duplicates).
        target (int): Value to search for.
        
    Returns:
        int: Index of last occurrence, or -1 if not found.
    """
    low = 0
    high = len(nums) - 1
    last_index = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            last_index = mid  # Record candidate
            low = mid + 1     # Continue searching in right half for a later occurrence
        elif nums[mid] < target:
            low = mid + 1     # Target is to the right
        else:
            high = mid - 1    # Target is to the left
            
    return last_index


def find_last_occurrence_bisect(nums: List[int], target: int) -> int:
    """
    Using Python's bisect_right:
    bisect_right returns the insertion position strictly greater than target.
    So the last occurrence of target, if present, is at index (idx - 1).
    """
    idx = bisect.bisect_right(nums, target)
    if idx > 0 and nums[idx - 1] == target:
        return idx - 1
    return -1


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Multiple duplicates in middle", [2, 4, 4, 4, 6, 7], 4, 3),
        ("Duplicates at start of array", [1, 1, 1, 2, 3], 1, 2),
        ("Duplicates at end of array", [1, 2, 3, 5, 5, 5], 5, 5),
        ("All elements are identical target", [7, 7, 7, 7, 7], 7, 4),
        ("Single target occurrence", [1, 3, 5, 7, 9], 5, 2),
        ("Target not present (in between)", [1, 2, 4, 5], 3, -1),
        ("Target smaller than all elements", [10, 20, 30], 5, -1),
        ("Target larger than all elements", [10, 20, 30], 40, -1),
        ("Single element found", [42], 42, 0),
        ("Single element not found", [42], 99, -1),
        ("Empty list", [], 5, -1),
    ]

    print("Running Tests for Problem 019: Last Occurrence of an Element\n" + "-" * 75)
    all_passed = True
    for name, nums, target, expected in test_cases:
        res_custom = find_last_occurrence(nums, target)
        res_bisect = find_last_occurrence_bisect(nums, target)
        
        passed = (res_custom == expected) and (res_bisect == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:34} | Target: {str(target):2} | Custom: {res_custom:2} | Bisect: {res_bisect:2} (Exp: {expected})")
        
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! ")
