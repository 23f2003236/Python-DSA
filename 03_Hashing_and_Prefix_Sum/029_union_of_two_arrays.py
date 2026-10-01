"""
Problem 029: Union of Two Arrays
Phase: 03_Hashing_and_Prefix_Sum
Difficulty: Easy
Core Concept: Set Operations / Hash Set / Two Pointers on Sorted Arrays

---
Problem Statement:
Given two integer arrays `nums1` and `nums2`, return an array containing their UNION.
The union of two arrays is a collection of all DISTINCT elements present in either array.

Example 1:
    Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 3]
    Output: [1, 2, 3, 4, 5]

Example 2:
    Input: nums1 = [85, 25, 1, 32, 54, 6], nums2 = [85, 2]
    Output: [1, 2, 6, 25, 32, 54, 85]

Example 3 (Arrays with duplicates):
    Input: nums1 = [1, 2, 1, 1, 2], nums2 = [2, 2, 1, 2, 1]
    Output: [1, 2]
---

Intuition & Approaches:

1. Approach 1: Hash Set (Optimal for Unsorted Arrays) 🧠
   - Combine unique elements using Python's set union:
     `return list(set(nums1) | set(nums2))`
   - Time Complexity: O(n + m)
   - Space Complexity: O(n + m) for the set.

2. Approach 2: Two Pointers (Optimal when Arrays are Pre-Sorted) 🤝
   - What if the interviewer asks: "What if the input arrays are already sorted and we want O(1) auxiliary space (excluding output)?"
   - Use two pointers `i = 0` (for nums1) and `j = 0` (for nums2):
     - If `nums1[i] < nums2[j]`:
       Add `nums1[i]` to union (skip if duplicate of last added), advance `i += 1`.
     - Else if `nums2[j] < nums1[i]`:
       Add `nums2[j]` to union (skip if duplicate of last added), advance `j += 1`.
     - Else (`nums1[i] == nums2[j]`):
       Add either one, advance both `i += 1` and `j += 1`.
     - Append any remaining unique elements from whichever array is not finished.
   - Time: O(n + m) if sorted (or O(n log n + m log m) with sorting).
   - Space: O(1) auxiliary space.

---
Complexity Analysis:
- Hash Set Method:
  - Time: O(n + m)
  - Space: O(n + m)
- Two Pointers Method (on sorted inputs):
  - Time: O(n + m)
  - Space: O(1) auxiliary space.
"""

from typing import List


def union_hashset(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Approach 1: Using Hash Set union.
    Time: O(n + m), Space: O(n + m).
    """
    return list(set(nums1) | set(nums2))


def union_two_pointers(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Approach 2: Two Pointers merge-style union on sorted arrays.
    Time: O(n + m) if pre-sorted, Space: O(1) auxiliary.
    """
    nums1.sort()
    nums2.sort()
    
    i = j = 0
    union_res = []
    
    def add_element(val: int):
        if not union_res or union_res[-1] != val:
            union_res.append(val)
            
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            add_element(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            add_element(nums2[j])
            j += 1
        else:
            add_element(nums1[i])
            i += 1
            j += 1
            
    # Add remaining elements from nums1
    while i < len(nums1):
        add_element(nums1[i])
        i += 1
        
    # Add remaining elements from nums2
    while j < len(nums2):
        add_element(nums2[j])
        j += 1
        
    return union_res


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("One array subset of another", [1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4, 5]),
        ("Partially overlapping arrays", [85, 25, 1, 32, 54, 6], [85, 2], [1, 2, 6, 25, 32, 54, 85]),
        ("Arrays with repeated elements", [1, 2, 1, 1, 2], [2, 2, 1, 2, 1], [1, 2]),
        ("Completely disjoint arrays", [1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ("Identical arrays", [5, 10, 15], [5, 10, 15], [5, 10, 15]),
        ("One empty array", [], [1, 2, 3], [1, 2, 3]),
        ("Both empty arrays", [], [], []),
    ]

    print("Running Tests for Problem 029: Union of Two Arrays\n" + "-" * 70)
    all_passed = True
    for name, nums1, nums2, expected in test_cases:
        res_set = union_hashset(list(nums1), list(nums2))
        res_tp = union_two_pointers(list(nums1), list(nums2))
        
        passed = (sorted(res_set) == sorted(expected)) and (sorted(res_tp) == sorted(expected))
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:32} | Result: {sorted(res_tp)} (Expected: {sorted(expected)})")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
