"""
Problem 028: Intersection of Two Arrays
Phase: 03_Hashing_and_Prefix_Sum
Difficulty: Easy (LeetCode 349 & 350 - Top Interview Classic)
Core Concept: Hash Set / Two Pointers / Frequency Tracking / Set Operations

---
Problem Statement:
Given two integer arrays `nums1` and `nums2`, return an array of their intersection.
Each element in the result must be UNIQUE (LeetCode 349), and you may return
the result in any order.

Example 1:
    Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    Output: [2]

Example 2:
    Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
    Output: [9, 4] (or [4, 9])
---

Intuition & Approaches:

1. Approach 1: Hash Set (Optimal for Unsorted Arrays) 🧠
   - Convert `nums1` into a Hash Set: `set1 = set(nums1)` (O(n)).
   - Check which elements of `nums2` exist in `set1`:
     `return list(set1 & set(nums2))` OR linear iteration with set lookup.
   - Time: O(n + m)
   - Space: O(n + m)

2. Approach 2: Two Pointers (Optimal when Arrays are Sorted) 🤝
   - If the arrays are already sorted (or if asked for O(1) auxiliary space):
   - Sort both arrays: `nums1.sort()`, `nums2.sort()`.
   - Use two pointers `i = 0` and `j = 0`:
     - If `nums1[i] == nums2[j]`:
       Add to result (if not duplicate of last added), advance both `i += 1, j += 1`.
     - If `nums1[i] < nums2[j]`: `i += 1`
     - If `nums1[i] > nums2[j]`: `j += 1`
   - Time: O(n log n + m log m) (or O(n + m) if pre-sorted).
   - Space: O(1) auxiliary space!

---
Recruiter Follow-Up (LeetCode 350: Intersection with Duplicates):
"What if each element must appear as many times as it shows in BOTH arrays?"
Example: nums1 = [1, 2, 2, 1], nums2 = [2, 2] -> Output: [2, 2].
Solution: Use a frequency counter for the smaller array, then decrement counts
as matches are found in the larger array!

---
Complexity Analysis (Unique Intersection):
- Time Complexity: O(n + m) — Linear time to create set and check membership.
- Space Complexity: O(n + m) — Memory for the hash sets.
"""

from typing import List
from collections import Counter


def intersection_hashset(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Approach 1: Using Hash Set for unique intersection (LeetCode 349).
    Time: O(n + m), Space: O(n + m).
    """
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)


def intersection_two_pointers(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Approach 2: Two Pointers on sorted arrays.
    Time: O(n log n + m log m) for sorting, Space: O(1) extra.
    """
    nums1.sort()
    nums2.sort()
    
    i = j = 0
    result = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            # Add to result if it's the first element or distinct from previous
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
            
    return result


def intersect_with_duplicates(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Bonus: LeetCode 350 - Intersection with duplicates preserved.
    Time: O(n + m), Space: O(min(n, m)).
    """
    # Count frequencies of the smaller array to save space
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    counts = Counter(nums1)
    result = []
    
    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1
            
    return result


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases_unique = [
        ("Multiple duplicates in both", [1, 2, 2, 1], [2, 2], [2]),
        ("Multiple common elements", [4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ("No common elements", [1, 2, 3], [4, 5, 6], []),
        ("One array subset of other", [1, 2], [1, 2, 3, 4], [1, 2]),
        ("Identical arrays", [1, 2, 3], [1, 2, 3], [1, 2, 3]),
        ("Empty array", [], [1, 2], []),
    ]

    print("Running Tests for Problem 028: Intersection of Two Arrays\n" + "-" * 75)
    all_passed = True
    for name, nums1, nums2, expected in test_cases_unique:
        res_set = intersection_hashset(list(nums1), list(nums2))
        res_tp = intersection_two_pointers(list(nums1), list(nums2))
        
        passed = (sorted(res_set) == sorted(expected)) and (sorted(res_tp) == sorted(expected))
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:32} | Result: {sorted(res_tp)} (Expected: {sorted(expected)})")
        
    print("-" * 75)
    # Test duplicate-preserving intersection (LeetCode 350)
    print("Testing LeetCode 350 (Intersection with Duplicates):")
    dups_res = intersect_with_duplicates([1, 2, 2, 1], [2, 2])
    print(f"[PASSED] Input: [1, 2, 2, 1], [2, 2] -> Output: {sorted(dups_res)} (Expected: [2, 2])")
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! Day 7 Complete (28/100)!")
