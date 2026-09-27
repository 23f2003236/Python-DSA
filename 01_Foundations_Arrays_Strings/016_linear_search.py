"""
Problem 016: Linear Search
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy
Core Concept: Sequential Traversal / Searching Fundamentals / Early Termination

---
Problem Statement:
Given an array (list) of elements `nums` and a target value `target`, return the
index of the first occurrence of `target` in the array.
If `target` is not present, return -1.

Example 1:
    Input: nums = [10, 50, 30, 70, 80, 20], target = 30
    Output: 2

Example 2:
    Input: nums = [10, 50, 30, 70, 80, 20], target = 99
    Output: -1

Example 3:
    Input: nums = [5, 2, 5, 2], target = 2
    Output: 1 (returns first occurrence index)
---

Intuition (Real-World Analogy: Looking for Keys in Pockets 🔑):
Imagine checking your pockets one by one:
1. You check pocket 0: Is the key here?
2. If yes, you stop immediately! (Early exit / Short-circuiting).
3. If no, you check pocket 1, then pocket 2, and so on.
4. If you check all pockets and find nothing, you conclude the key is missing (-1).

---
When does Linear Search Beat Binary Search? 🧠
1. Unsorted Arrays:
   Binary Search REQUIREs the array to be sorted (O(n log n) sorting cost).
   If you only need to search once in an unsorted array, Linear Search (O(n)) is faster than Sorting + Binary Search!
2. Very Small Arrays (n <= 16):
   Linear scan has fantastic CPU cache locality and zero branching overhead, making it faster in practice for small inputs.

---
Complexity Analysis:
- Best Case Time: O(1) — When target is at index 0.
- Worst Case Time: O(n) — When target is at the last index or not present.
- Average Case Time: O(n) — On average, we search through n/2 elements.
- Space Complexity: O(1) — Constant memory.
"""

from typing import List, Any


def linear_search(nums: List[Any], target: Any) -> int:
    """
    Searches for target in nums sequentially.
    
    Args:
        nums (List[Any]): List of elements to search through.
        target (Any): The element to search for.
        
    Returns:
        int: Index of first occurrence, or -1 if not found.
    """
    for index, value in enumerate(nums):
        if value == target:
            return index  # Early termination on first match
            
    return -1


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Target in middle", [10, 50, 30, 70, 80, 20], 30, 2),
        ("Target at beginning", [42, 10, 20], 42, 0),
        ("Target at very end", [10, 20, 99], 99, 2),
        ("Target not found", [1, 2, 3, 4], 100, -1),
        ("Multiple occurrences (returns first)", [5, 2, 5, 2], 2, 1),
        ("Strings search", ["apple", "banana", "cherry"], "banana", 1),
        ("Negative numbers", [-10, -20, -5, 0], -5, 2),
        ("Empty list", [], 10, -1),
    ]

    print("Running Tests for Problem 016: Linear Search\n" + "-" * 70)
    all_passed = True
    for name, nums, target, expected in test_cases:
        actual = linear_search(nums, target)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:33} | Target: {str(target):5} | Index: {actual:2} (Expected: {expected})")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! Phase 1 Complete (16/16)!")
