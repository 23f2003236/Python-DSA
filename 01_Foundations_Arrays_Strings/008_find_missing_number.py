"""
Problem 008: Find Missing Number
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy (LeetCode 268 - Top Interview Classic)
Core Concept: Math (Gauss Formula) / Bitwise XOR (Cancellation)

---
Problem Statement:
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`,
return the only number in the range that is missing from the array.

Example 1:
    Input: nums = [3, 0, 1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers. Range is [0, 3].
                 0, 1, and 3 are present. 2 is missing.

Example 2:
    Input: nums = [0, 1]
    Output: 2
    Explanation: n = 2. Range is [0, 2]. 2 is missing.

Example 3:
    Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    Output: 8
---

Approach 1: Math Sum (Gauss Formula) 🧮
- The sum of numbers from 0 to n is:
      expected_sum = n * (n + 1) // 2
- The actual sum of elements in `nums`:
      actual_sum = sum(nums)
- Missing number:
      missing = expected_sum - actual_sum

Time: O(n), Space: O(1).
Caveat: In languages like C++/Java with fixed 32-bit integers, n * (n + 1) can overflow!

---
Approach 2: Bitwise XOR Cancellation (The Interviewer's Favorite! ⚡)
Remember XOR properties:
1. a ^ a = 0 (Any number XORed with itself cancels to 0)
2. a ^ 0 = a (Any number XORed with 0 remains unchanged)
3. XOR is commutative and associative (order does not matter).

Algorithm:
- Initialize `xor_all = 0`.
- XOR all numbers from 0 to n:
      0 ^ 1 ^ 2 ^ ... ^ n
- XOR all numbers present in `nums`:
      nums[0] ^ nums[1] ^ ... ^ nums[n-1]
- Every number that is present in both sets will cancel out (x ^ x = 0)!
- The ONLY number that appears once is the missing number!
- Bonus: ZERO risk of integer overflow!

Time: O(n), Space: O(1).
"""

from typing import List


def find_missing_number_math(nums: List[int]) -> int:
    """
    Finds the missing number using Gauss's summation formula.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def find_missing_number_xor(nums: List[int]) -> int:
    """
    Finds the missing number using Bitwise XOR cancellation (Optimal & Overflow-safe).
    """
    n = len(nums)
    xor_result = 0
    
    # XOR all expected numbers in range [0, n]
    for i in range(n + 1):
        xor_result ^= i
        
    # XOR all actual numbers in nums
    for num in nums:
        xor_result ^= num
        
    return xor_result


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Missing in middle", [3, 0, 1], 2),
        ("Missing n at end", [0, 1], 2),
        ("Missing 0 at start", [1, 2, 3], 0),
        ("Larger array", [9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ("Single element: missing 1", [0], 1),
        ("Single element: missing 0", [1], 0),
        ("Two elements: missing 1", [0, 2], 1),
    ]

    print("Running Tests for Problem 008: Find Missing Number\n" + "-" * 65)
    all_passed = True
    for name, nums, expected in test_cases:
        res_math = find_missing_number_math(nums)
        res_xor = find_missing_number_xor(nums)
        
        passed = (res_math == expected) and (res_xor == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:28} | Math: {res_math} | XOR: {res_xor} | Expected: {expected}")
        
    print("-" * 65)
    if all_passed:
        print("All test cases passed successfully! Day 2 Complete (8/100)!")
