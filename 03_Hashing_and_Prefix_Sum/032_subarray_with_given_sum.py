"""
Problem 032: Subarray With Given Sum
Phase: 03_Hashing_and_Prefix_Sum
Difficulty: Medium (Classic Interview Pattern)
Core Concept: Sliding Window (Positive Only) vs. Prefix Sum + Hash Map (Universal)

---
Problem Statement:
Given an array of integers `nums` and an integer `target_sum`, find a continuous
subarray that adds up to `target_sum`.
Return the 0-based start and end indices `[start, end]` of the first such subarray.
If no such subarray exists, return `[-1, -1]`.

Example 1:
    Input: nums = [1, 2, 3, 7, 5], target_sum = 12
    Output: [1, 3]
    Explanation: nums[1] + nums[2] + nums[3] = 2 + 3 + 7 = 12.

Example 2 (With negative numbers):
    Input: nums = [10, 2, -2, -20, 10], target_sum = -10
    Output: [0, 3]
    Explanation: 10 + 2 + (-2) + (-20) = -10.

Example 3 (Not found):
    Input: nums = [1, 2, 3], target_sum = 10
    Output: [-1, -1]
---

Intuition & The Critical Recruiter Distinction ⚠️:

Case A: Array contains ONLY POSITIVE / Non-Negative numbers
- Adding an element ALWAYS increases the sum.
- Removing an element ALWAYS decreases the sum.
- We can use a **Variable Sliding Window (Two Pointers)**:
  Expand `right`: add `nums[right]` to `curr_sum`.
  While `curr_sum > target_sum` and `left <= right`:
      subtract `nums[left]` from `curr_sum`, increment `left += 1`.
  If `curr_sum == target_sum`: return `[left, right]`.
- Time: O(n), Space: **O(1)** strictly!

Case B: Array contains NEGATIVE numbers or Zeros
- Sliding window FAILS because adding a negative number decreases the sum,
  breaking the monotonic window property!
- We MUST use **Prefix Sum + Hash Map**:
  Let `running_sum[i]` be the sum of nums[0...i].
  If `running_sum[i] - target_sum` was seen earlier at index `j`,
  then the sum of elements from index `j + 1` to `i` is EXACTLY `target_sum`!
- Maintain a map: `{running_sum: index}`.
- Time: O(n), Space: O(n).

---
Complexity Analysis:
- Sliding Window (Positive numbers only):
  - Time: O(n)
  - Space: O(1)
- Prefix Sum + Hash Map (Handles negative numbers):
  - Time: O(n)
  - Space: O(n)
"""

from typing import List


def subarray_sum_sliding_window(nums: List[int], target_sum: int) -> List[int]:
    """
    Approach 1: Variable Sliding Window.
    Optimal for arrays with non-negative numbers only.
    Time: O(n), Space: O(1).
    """
    left = 0
    curr_sum = 0
    
    for right in range(len(nums)):
        curr_sum += nums[right]
        
        # Shrink window from the left if sum exceeds target
        while curr_sum > target_sum and left < right:
            curr_sum -= nums[left]
            left += 1
            
        if curr_sum == target_sum:
            return [left, right]
            
    return [-1, -1]


def subarray_sum_prefix_map(nums: List[int], target_sum: int) -> List[int]:
    """
    Approach 2: Prefix Sum + Hash Map.
    Universal approach that handles positive, negative, and zero values.
    Time: O(n), Space: O(n).
    """
    # prefix_map stores {running_sum: index}
    # Initialize with sum 0 at index -1 to handle subarrays starting at index 0
    prefix_map = {0: -1}
    running_sum = 0
    
    for i, num in enumerate(nums):
        running_sum += num
        needed_prefix = running_sum - target_sum
        
        if needed_prefix in prefix_map:
            start_index = prefix_map[needed_prefix] + 1
            return [start_index, i]
            
        # Only record first occurrence of running_sum (optional for length, standard practice)
        if running_sum not in prefix_map:
            prefix_map[running_sum] = i
            
    return [-1, -1]


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    # Tests for positive numbers (both algorithms should pass)
    test_cases_positives = [
        ("Subarray in middle", [1, 2, 3, 7, 5], 12, [1, 3]),
        ("Subarray at start", [5, 2, 3, 1], 7, [0, 1]),
        ("Single element match", [1, 4, 20, 3, 10, 5], 20, [2, 2]),
        ("Entire array", [1, 2, 3, 4], 10, [0, 3]),
        ("No matching subarray", [1, 2, 3], 10, [-1, -1]),
    ]

    print("Running Tests for Problem 032: Subarray With Given Sum\n" + "-" * 75)
    all_passed = True
    print("[Testing Positive Numbers - Sliding Window & Prefix Map]")
    for name, nums, target, expected in test_cases_positives:
        res_sw = subarray_sum_sliding_window(nums, target)
        res_pm = subarray_sum_prefix_map(nums, target)
        
        passed = (res_sw == expected) and (res_pm == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:25} | Target: {target:2} | SW: {res_sw} | PM: {res_pm}")

    # Tests with negative numbers (Prefix Map should pass)
    test_cases_negatives = [
        ("Array with negative numbers", [10, 2, -2, -20, 10], -10, [0, 3]),
        ("Negative target sum", [-10, -5, -2, 0, 3], -15, [0, 1]),
        ("Zero sum subarray", [1, 4, -4, 2], 0, [1, 2]),
    ]
    print("\n[Testing Negative Numbers - Prefix Map Universal]")
    for name, nums, target, expected in test_cases_negatives:
        res_pm = subarray_sum_prefix_map(nums, target)
        passed = (res_pm == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:30} | Target: {target:3} | Result: {res_pm} (Exp: {expected})")
        
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! Day 8 Complete (32/100)!")
