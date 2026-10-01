"""
Problem 030: Majority Element (> n/2)
Phase: 03_Hashing_and_Prefix_Sum
Difficulty: Easy (LeetCode 169 - Top Interview Classic)
Core Concept: Boyer-Moore Voting Algorithm / Cancellation Principle / Constant Space

---
Problem Statement:
Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Follow-up Challenge: Could you solve the problem in linear time O(n) and in O(1) space?

Example 1:
    Input: nums = [3, 2, 3]
    Output: 3

Example 2:
    Input: nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2

Example 3:
    Input: nums = [1]
    Output: 1
---

Intuition (The Battle Royale Analogy ⚔️):
If an element appears more than n / 2 times, it has strictly MORE occurrences than
ALL OTHER ELEMENTS COMBINED!

Imagine an arena:
- Every time two fighters from different factions meet, they fight and both fall (cancel each other out).
- Because the majority faction has MORE than 50% of all fighters:
  Even if EVERY single non-majority fighter takes down one majority fighter,
  there will STILL be majority fighters standing at the end!

---
The Boyer-Moore Voting Algorithm 🗳️:
1. Maintain two variables:
   `candidate = None`
   `count = 0`
2. Iterate through `nums`:
   - If `count == 0`:
     The current faction is wiped out! Pick the current element as the new `candidate`, and set `count = 1`.
   - Else if `num == candidate`:
     An ally has arrived! Increment `count += 1`.
   - Else:
     An enemy has arrived! They cancel each other out: Decrement `count -= 1`.
3. At the end of the array, `candidate` is guaranteed to be the majority element!

---
Comparison of Approaches:
| Approach | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- |
| **1. Hash Map / Counter** | O(n) | O(n) | Uses extra memory |
| **2. Sorting (`nums[n // 2]`)** | O(n log n) | O(1) or O(n) | Clever, but slower than O(n) |
| **3. Boyer-Moore Voting** | **O(n)** | **O(1)** | ✅ **Optimal & Legendary** |

---
Complexity Analysis:
- Time Complexity: O(n) — A single pass through the array.
- Space Complexity: O(1) — Uses only two primitive variables (`candidate` and `count`).
"""

from typing import List, Optional
from collections import Counter


def majority_element_hashmap(nums: List[int]) -> int:
    """
    Approach 1: Using Hash Map / Counter.
    Time: O(n), Space: O(n).
    """
    counts = Counter(nums)
    n = len(nums)
    for num, count in counts.items():
        if count > n // 2:
            return num
    return -1


def majority_element_sorting(nums: List[int]) -> int:
    """
    Approach 2: Sorting.
    Since majority appears > n/2 times, it must occupy the middle index!
    Time: O(n log n), Space: O(1) or O(n).
    """
    nums.sort()
    return nums[len(nums) // 2]


def majority_element_boyer_moore(nums: List[int]) -> Optional[int]:
    """
    Approach 3: Boyer-Moore Voting Algorithm (Optimal O(n) time, O(1) space).
    """
    candidate = None
    count = 0
    
    # Phase 1: Find candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
            
    # Phase 2 (Optional verification if majority is not guaranteed):
    # Here the problem guarantees majority exists, but in general interviews:
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard small array", [3, 2, 3], 3),
        ("Standard medium array", [2, 2, 1, 1, 1, 2, 2], 2),
        ("Single element array", [1], 1),
        ("Majority barely over half", [1, 2, 1, 3, 1], 1),
        ("All identical elements", [9, 9, 9, 9], 9),
        ("Negative numbers in array", [-1, -1, 2, -1], -1),
        ("Alternating pattern", [6, 5, 5], 5),
    ]

    print("Running Tests for Problem 030: Majority Element (Boyer-Moore)\n" + "-" * 75)
    all_passed = True
    for name, nums, expected in test_cases:
        res_hm = majority_element_hashmap(list(nums))
        res_sort = majority_element_sorting(list(nums))
        res_bm = majority_element_boyer_moore(list(nums))
        
        passed = (res_hm == expected) and (res_sort == expected) and (res_bm == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:30} | Input: {str(nums):24} | Result: {res_bm} (Expected: {expected})")
        
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! ")
