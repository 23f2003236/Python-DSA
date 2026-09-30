"""
Problem 027: Three Sum (3Sum)
Phase: 03_Hashing_and_Prefix_Sum
Difficulty: Medium (LeetCode 15 - Top FAANG Interview Classic)
Core Concept: Sorting + Two Pointers / Duplicate Elimination / Target Matching

---
Problem Statement:
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]`
such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must NOT contain duplicate triplets!

Example 1:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Example 2:
    Input: nums = [0, 1, 1]
    Output: []

Example 3:
    Input: nums = [0, 0, 0]
    Output: [[0, 0, 0]]
---

Intuition (Fix One Person + Two Pointers 🎯):
Brute force checking all triplets takes O(n^3) time.
Instead, we can reduce 3Sum to Two Sum!

1. Sort the array first: `nums.sort()` (O(n log n)).
   Sorting allows us to:
   a) Use the Two Pointers technique on the rest of the array.
   b) Easily skip duplicate numbers to avoid duplicate triplets!
2. Fix the first element `nums[i]` in a loop:
   Now the problem becomes:
   "Find two numbers in nums[i+1 ... n-1] whose sum is equal to -nums[i]!"
3. Use two pointers (`left = i + 1`, `right = n - 1`):
   - `total = nums[i] + nums[left] + nums[right]`
   - If `total == 0`: Found a triplet! Record it.
     Then advance `left` and `right` while skipping adjacent identical elements.
   - If `total < 0`: Sum is too small -> move `left += 1`.
   - If `total > 0`: Sum is too large -> move `right -= 1`.

---
The #1 Trap: Avoiding Duplicate Triplets ⚠️
1. Outer Loop duplicate skip:
   `if i > 0 and nums[i] == nums[i - 1]: continue`
2. Inner Loop duplicate skips:
   After finding a triplet:
   `while left < right and nums[left] == nums[left + 1]: left += 1`
   `while left < right and nums[right] == nums[right - 1]: right -= 1`
   `left += 1`
   `right -= 1`
3. Early Exit:
   If `nums[i] > 0`: Since the array is sorted, all subsequent elements are also > 0.
   Three positive numbers can NEVER sum to 0 -> break immediately!

---
Complexity Analysis:
- Time Complexity: O(n^2) — Sorting takes O(n log n), and the outer loop runs n times with an O(n) two-pointer scan.
- Space Complexity: O(1) or O(n) — O(1) auxiliary space (ignoring space used by sorting and output list).
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in nums that sum up to 0 using Sorting + Two Pointers.
    
    Args:
        nums (List[int]): Array of integers.
        
    Returns:
        List[List[int]]: List of unique triplets.
    """
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 2):
        # Optimization: Since array is sorted, if nums[i] > 0, sum can never be 0
        if nums[i] > 0:
            break
            
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left = i + 1
        right = n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicate values for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate values for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif total < 0:
                left += 1   # Need a larger sum
            else:
                right -= 1  # Need a smaller sum
                
    return result


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard case with multiple triplets", [-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ("No triplets summing to zero", [0, 1, 1], []),
        ("All zeros", [0, 0, 0, 0], [[0, 0, 0]]),
        ("Array with negative numbers only", [-5, -2, -1], []),
        ("Array with positive numbers only", [1, 2, 3, 4], []),
        ("Multiple duplicates", [-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ("Less than 3 elements", [1, -1], []),
        ("Empty list", [], []),
    ]

    print("Running Tests for Problem 027: Three Sum\n" + "-" * 70)
    all_passed = True
    for name, nums, expected in test_cases:
        actual = three_sum(list(nums))
        
        # Sort internal triplets and external list for unbiased comparison
        sorted_actual = sorted([sorted(t) for t in actual])
        sorted_expected = sorted([sorted(t) for t in expected])
        
        passed = sorted_actual == sorted_expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:38} | Result: {actual} (Exp: {expected})")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
