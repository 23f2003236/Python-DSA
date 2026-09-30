"""
Problem 025: Quick Sort (Partitioning & Pivot Selection — Phase 2 Finale)
Phase: 02_Searching_and_Sorting
Difficulty: Medium
Core Concept: Divide and Conquer / Lomuto Partitioning / In-place Array Mutation / Randomized Pivot

---
Problem Statement:
Given an array of integers `nums`, sort the array in ascending order using Quick Sort.
The sorting must be performed IN-PLACE.

Example 1:
    Input: nums = [10, 7, 8, 9, 1, 5]
    Output: [1, 5, 7, 8, 9, 10]

Example 2:
    Input: nums = [5, 2, 3, 1]
    Output: [1, 2, 3, 5]

Example 3:
    Input: nums = [5, 1, 1, 2, 0, 0]
    Output: [0, 0, 1, 1, 2, 5]
---

Intuition (The Class Captain / Benchmark Analogy 🎯):
Quick Sort is a Divide-and-Conquer algorithm based on one central idea: **Partitioning**.

1. Choose a `pivot` element (e.g., the last element `nums[high]`).
2. Partition the array:
   - Rearrange elements such that all elements `< pivot` move to the LEFT of pivot.
   - All elements `> pivot` move to the RIGHT of pivot.
   - The pivot settles into its EXACT final sorted position!
3. Recursively repeat the same process for:
   - The left subarray (from `low` to `pivot_index - 1`)
   - The right subarray (from `pivot_index + 1` to `high`)

---
Lomuto Partition Scheme (Step-by-Step):
Let pivot = nums[high].
- Maintain pointer `i = low - 1` (tracks boundary of elements smaller than pivot).
- Scan `j` from `low` to `high - 1`:
  - If `nums[j] <= pivot`:
    - Increment `i += 1`
    - Swap `nums[i]` and `nums[j]`
- Finally, place pivot in its rightful place: swap `nums[i + 1]` with `nums[high]`.
- Return `i + 1` (the pivot's final index).

---
Recruiter Deep Dive 🔥: Quick Sort vs Merge Sort

| Criteria | Quick Sort | Merge Sort |
| :--- | :--- | :--- |
| **Average Time** | O(n log n) | O(n log n) |
| **Worst Time** | O(n^2) (if pivot is consistently min/max) | O(n log n) guaranteed |
| **Auxiliary Space** | **O(log n)** (call stack only - IN-PLACE!) | O(n) extra array memory |
| **Cache Locality** | Superb (cache-friendly contiguous access) | Poor (creates new arrays) |
| **Stability** | Unstable | Stable |

Why does C++ `std::sort` and Java primitive `Arrays.sort` use QuickSort / Dual-Pivot QuickSort?
Because in real hardware, QuickSort's in-place cache locality makes it 2x to 3x faster than Merge Sort!

---
Complexity Analysis:
- Best Case Time: O(n log n) — Pivot divides array into two equal halves.
- Average Case Time: O(n log n).
- Worst Case Time: O(n^2) — Already sorted array with worst pivot choice (alleviated by randomized pivot).
- Space Complexity: O(log n) call stack on average (O(n) worst-case call stack).
"""

from typing import List
import random


def partition_lomuto(nums: List[int], low: int, high: int) -> int:
    """
    Partitions the subarray nums[low...high] around a pivot using Lomuto's scheme.
    Returns the final index of the pivot.
    """
    # Randomized Pivot: Pick a random index between low and high, and swap with high
    # This prevents the O(n^2) worst-case on already sorted arrays!
    rand_idx = random.randint(low, high)
    nums[rand_idx], nums[high] = nums[high], nums[rand_idx]
    
    pivot = nums[high]
    i = low - 1  # Index of smaller element boundary
    
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            
    # Swap pivot into its correct final position
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quick_sort_helper(nums: List[int], low: int, high: int) -> None:
    """
    Recursive helper for in-place Quick Sort.
    """
    if low < high:
        # pi is the partitioning index; nums[pi] is now at the right place
        pi = partition_lomuto(nums, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort_helper(nums, low, pi - 1)
        quick_sort_helper(nums, pi + 1, high)


def quick_sort(nums: List[int]) -> List[int]:
    """
    Sorts nums in-place using Quick Sort.
    
    Args:
        nums (List[int]): Array to be sorted.
        
    Returns:
        List[int]: The sorted array reference.
    """
    if len(nums) <= 1:
        return nums
        
    quick_sort_helper(nums, 0, len(nums) - 1)
    return nums


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard unsorted array", [10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),
        ("Already sorted (tests randomized pivot)", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("Reverse sorted array", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ("Array with multiple duplicates", [5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
        ("Negative numbers", [-5, 10, -20, 0, 3], [-20, -5, 0, 3, 10]),
        ("All identical elements", [7, 7, 7, 7], [7, 7, 7, 7]),
        ("Two elements", [2, 1], [1, 2]),
        ("Single element array", [42], [42]),
        ("Empty array", [], []),
    ]

    print("Running Tests for Problem 025: Quick Sort\n" + "-" * 70)
    all_passed = True
    for name, original, expected in test_cases:
        arr_copy = list(original)
        actual = quick_sort(arr_copy)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:32} | Input: {str(original):25} | Sorted: {actual}")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! Phase 2 Complete (25/100)!")
