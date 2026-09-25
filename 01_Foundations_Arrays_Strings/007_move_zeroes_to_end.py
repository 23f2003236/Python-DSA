"""
Problem 007: Move Zeroes to End
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy (LeetCode 283 - Top Interview Classic)
Core Concept: Two Pointers / Partitioning / In-place Mutation

---
Problem Statement:
Given an integer array `nums`, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.
You must do this IN-PLACE without making a copy of the array.

Example 1:
    Input: nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Example 2:
    Input: nums = [0]
    Output: [0]

Example 3:
    Input: nums = [1, 2, 3]
    Output: [1, 2, 3]
---

Intuition (Real-World Analogy: Snowplow / Bubble Clearer 🚜):
Think of cleaning a conveyor belt with items and empty gaps (zeros):
- Pointer `non_zero_pos` keeps track of where the next non-zero item should be placed.
- Pointer `current` scans across the array:
  - If `nums[current] == 0`: Just ignore and keep moving forward.
  - If `nums[current] != 0`: We found a valid non-zero element!
    Swap `nums[non_zero_pos]` with `nums[current]`.
    Advance `non_zero_pos += 1`.

Why swapping works beautifully:
1. When all initial elements are non-zero (e.g., [1, 2, 3]), `non_zero_pos == current`,
   so each element swaps with itself (no disruption).
2. The moment a 0 is found, `non_zero_pos` pauses at that 0 while `current` moves ahead.
3. When `current` finds the next non-zero, swapping puts the non-zero at `non_zero_pos`
   and moves the 0 further down the line!

---
Comparison of Approaches:
| Approach | Time | Space | Notes |
| :--- | :--- | :--- | :--- |
| 1. Extra Array `[x for x in nums if x != 0] + [0] * k` | O(n) | O(n) | Violates in-place requirement! |
| 2. Count Zeros + Overwrite | O(n) | O(1) | Two passes (write non-zeros, then fill rest with 0). |
| 3. Two-Pointer Swap (Optimal) | O(n) | O(1) | Single pass, minimal writes, preserves order. |

---
Complexity Analysis:
- Time Complexity: O(n) — Single linear scan over n elements.
- Space Complexity: O(1) — Strictly in-place modification.
"""

from typing import List


def move_zeroes(nums: List[int]) -> List[int]:
    """
    Moves all zeroes in nums to the end in-place while preserving relative order.
    
    Args:
        nums (List[int]): Input array of integers.
        
    Returns:
        List[int]: The modified array reference.
    """
    non_zero_pos = 0  # Where the next non-zero element should be placed
    
    # Iterate through the array
    for current in range(len(nums)):
        if nums[current] != 0:
            # Swap non-zero element with the element at non_zero_pos
            nums[non_zero_pos], nums[current] = nums[current], nums[non_zero_pos]
            non_zero_pos += 1
            
    return nums


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Mixed zeroes and positives", [0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ("Single zero", [0], [0]),
        ("No zeroes", [1, 2, 3, 4], [1, 2, 3, 4]),
        ("All zeroes", [0, 0, 0, 0], [0, 0, 0, 0]),
        ("Leading zeroes", [0, 0, 1], [1, 0, 0]),
        ("Trailing zeroes", [1, 2, 0, 0], [1, 2, 0, 0]),
        ("Negative numbers with zeroes", [0, -1, 0, -3, 12], [-1, -3, 12, 0, 0]),
        ("Empty array", [], []),
    ]

    print("Running Tests for Problem 007: Move Zeroes to End\n" + "-" * 65)
    all_passed = True
    for name, original, expected in test_cases:
        arr_copy = list(original)
        actual = move_zeroes(arr_copy)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:30} | Before: {str(original):20} | After: {actual}")
        
    print("-" * 65)
    if all_passed:
        print("All test cases passed successfully!")
