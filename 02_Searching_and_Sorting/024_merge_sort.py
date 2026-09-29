"""
Problem 024: Merge Sort (Divide & Conquer / O(n log n) Masterclass)
Phase: 02_Searching_and_Sorting
Difficulty: Medium
Core Concept: Divide and Conquer / Recursion / Two-Pointer Merging / Guaranteed O(n log n)

---
Problem Statement:
Given an array of integers `nums`, sort the array in ascending order using Merge Sort.

Example 1:
    Input: nums = [38, 27, 43, 3, 9, 82, 10]
    Output: [3, 9, 10, 27, 38, 43, 82]

Example 2:
    Input: nums = [5, 2, 3, 1]
    Output: [1, 2, 3, 5]

Example 3:
    Input: nums = [5, 1, 1, 2, 0, 0]
    Output: [0, 0, 1, 1, 2, 5]
---

Intuition (Divide and Conquer ⚔️):
Sorting an entire array of size 1,000,000 all at once is complicated.
However, sorting an array of size 1 is TRIVIAL (it is already sorted!).

Merge Sort breaks down the problem in 3 clear steps:
1. Divide:
   Find the middle index and split the array into two halves:
   `left_half = nums[:mid]`
   `right_half = nums[mid:]`
2. Conquer:
   Recursively call `merge_sort` on both halves until base case (`len(nums) <= 1`) is reached.
3. Combine (Merge):
   Merge the two sorted halves into a single sorted array using the Two Pointers technique in O(n) time!

---
The Two-Pointer Merge Step 🤝:
Given two sorted arrays `left` and `right`:
- Pointer `i` at `left[0]`, pointer `j` at `right[0]`.
- Compare `left[i]` and `right[j]`.
- Whichever is smaller, append it to `merged` and advance its pointer.
- Crucial for Stability: If `left[i] == right[j]`, pick from `left` first!
  This preserves the relative order of duplicate elements.
- Once one array is exhausted, append the remaining elements of the other array.

---
Complexity Analysis:
- Recurrence Relation: T(n) = 2T(n/2) + O(n)
- Best Case Time: O(n log n)
- Worst Case Time: O(n log n) — Guaranteed! (Unlike Quick Sort which degrades to O(n^2)).
- Average Case Time: O(n log n)
- Auxiliary Space: O(n) — Required to store temporary arrays during merge.
- Stability: STABLE!
"""

from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list in O(n) time.
    Maintains stability by taking from left list when elements are equal.
    """
    merged = []
    i = j = 0
    
    # Traverse both arrays and pick the smaller element
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # '<=' ensures stability!
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged


def merge_sort(nums: List[int]) -> List[int]:
    """
    Recursively sorts nums using Merge Sort.
    
    Args:
        nums (List[int]): Array to be sorted.
        
    Returns:
        List[int]: New sorted array.
    """
    # Base case: Arrays with 0 or 1 element are already sorted
    if len(nums) <= 1:
        return nums
        
    # Divide: Split into two halves
    mid = len(nums) // 2
    left_sorted = merge_sort(nums[:mid])
    right_sorted = merge_sort(nums[mid:])
    
    # Conquer & Combine: Merge the two sorted halves
    return merge(left_sorted, right_sorted)


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard unsorted array", [38, 27, 43, 3, 9, 82, 10], [3, 9, 10, 27, 38, 43, 82]),
        ("Reverse sorted array", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ("Already sorted array", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("Array with multiple duplicates", [5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
        ("Negative numbers", [-5, 10, -20, 0, 3], [-20, -5, 0, 3, 10]),
        ("All identical elements", [7, 7, 7, 7], [7, 7, 7, 7]),
        ("Two elements", [2, 1], [1, 2]),
        ("Single element array", [42], [42]),
        ("Empty array", [], []),
    ]

    print("Running Tests for Problem 024: Merge Sort\n" + "-" * 70)
    all_passed = True
    for name, nums, expected in test_cases:
        actual = merge_sort(nums)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:32} | Input: {str(nums):25} | Sorted: {actual}")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! Day 6 Complete (24/100)!")
