"""
Problem 017: Binary Search (Iterative & Recursive)
Phase: 02_Searching_and_Sorting
Difficulty: Easy (LeetCode 704 - Core Foundational Pattern)
Core Concept: Divide and Conquer / Search Space Halving / Invariant Maintenance

---
Problem Statement:
Given an array of integers `nums` which is sorted in ascending order, and an integer
`target`, write a function to search `target` in `nums`.
If `target` exists, return its index. Otherwise, return -1.
Runtime complexity must be O(log n).

Example 1:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4.

Example 2:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1.
---

Intuition (Real-World Analogy: Guess the Number 1 to 100 🎯):
Imagine a game where someone picks a secret number between 1 and 100:
- If you guess 1, 2, 3... (Linear Search), it could take 100 guesses in the worst case!
- Instead, you guess the MIDPOINT: 50!
  - If the host says "Higher", you instantly eliminate 1 to 50! (50% of the possibilities gone in 1 step).
  - Next, you guess the midpoint of [51, 100], which is 75!
  - Each step cuts the remaining search space strictly in HALF.
- For 1,000,000 items:
  Linear Search = up to 1,000,000 checks.
  Binary Search = at most 20 checks! (log2(1,000,000) ≈ 20).

---
Why `mid = low + (high - low) // 2` instead of `(low + high) // 2`? ⚠️
In Python, integers have arbitrary precision so overflow is rare.
HOWEVER, in C++, Java, and Go, `low + high` can exceed 2^31 - 1, causing an integer overflow bug!
Writing `low + (high - low) // 2` proves to the interviewer that you write robust, production-grade code.

---
Iterative vs. Recursive:
| Approach | Time Complexity | Auxiliary Space | Call Stack Overhead |
| :--- | :--- | :--- | :--- |
| **Iterative** | O(log n) | **O(1)** | None (Preferred in industry) |
| **Recursive** | O(log n) | **O(log n)** | log n stack frames |

---
Complexity Analysis:
- Time Complexity: O(log n) — The search space is divided by 2 in each iteration.
- Space Complexity:
    - Iterative: O(1) constant extra space.
    - Recursive: O(log n) stack frames due to recursion.
"""

from typing import List


def binary_search_iterative(nums: List[int], target: int) -> int:
    """
    Performs standard binary search iteratively.
    Time: O(log n), Space: O(1).
    """
    low = 0
    high = len(nums) - 1
    
    # Invariant: If target is in nums, it must be within nums[low...high]
    while low <= high:
        # Avoid integer overflow
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] < target:
            low = mid + 1   # Search right half
        else:
            high = mid - 1  # Search left half
            
    return -1  # Target not found


def binary_search_recursive(nums: List[int], target: int) -> int:
    """
    Performs standard binary search recursively.
    Time: O(log n), Space: O(log n) due to call stack.
    """
    def search_helper(low: int, high: int) -> int:
        if low > high:
            return -1  # Base case: Search space exhausted
            
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return search_helper(mid + 1, high)
        else:
            return search_helper(low, mid - 1)
            
    return search_helper(0, len(nums) - 1)


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Target in right half", [-1, 0, 3, 5, 9, 12], 9, 4),
        ("Target not found (in between)", [-1, 0, 3, 5, 9, 12], 2, -1),
        ("Target at beginning (index 0)", [10, 20, 30, 40, 50], 10, 0),
        ("Target at end (index n-1)", [10, 20, 30, 40, 50], 50, 4),
        ("Target exactly in middle", [1, 3, 5, 7, 9], 5, 2),
        ("Single element found", [42], 42, 0),
        ("Single element not found", [42], 99, -1),
        ("Target smaller than all elements", [10, 20, 30], 5, -1),
        ("Target larger than all elements", [10, 20, 30], 50, -1),
        ("Empty array", [], 7, -1),
    ]

    print("Running Tests for Problem 017: Binary Search\n" + "-" * 70)
    all_passed = True
    for name, nums, target, expected in test_cases:
        res_iter = binary_search_iterative(nums, target)
        res_rec = binary_search_recursive(nums, target)
        
        passed = (res_iter == expected) and (res_rec == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:32} | Target: {str(target):3} | Result: {res_iter:2} (Expected: {expected})")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
