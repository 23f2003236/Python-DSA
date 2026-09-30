"""
Problem 026: Two Sum
Phase: 03_Hashing_and_Prefix_Sum
Difficulty: Easy (LeetCode #1 - The Most Famous Interview Problem in History)
Core Concept: Hash Map Complement Lookup / Trade Space for Time

---
Problem Statement:
Given an array of integers `nums` and an integer `target`, return indices of the
two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not
use the same element twice. You can return the answer in any order.

Example 1:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]

Example 3:
    Input: nums = [3, 3], target = 6
    Output: [0, 1]
---

Intuition (The Missing Puzzle Piece Analogy 🧩):
Suppose target is 9.
When you see the number 2 at index 0, what number are you desperately looking for?
`complement = target - current_num = 9 - 2 = 7`!

Instead of scanning through the rest of the array with a nested loop (which takes O(n^2)),
we maintain a Hash Map (`seen = {}`) of people we have already met:
`{number: index}`

At each step:
1. Calculate `complement = target - num`.
2. Check: "Is complement already in my Hash Map?"
   - YES: We found the pair! Return `[seen[complement], current_index]`.
   - NO: Record current number in Hash Map (`seen[num] = current_index`) and move on.

---
Why Single Pass avoids the "Same Element Twice" Trap ⚠️:
If nums = [3, 3] and target = 6:
- At index 0 (val = 3): complement is 3. `3 in seen` is False (seen is empty).
  Add `seen[3] = 0`.
- At index 1 (val = 3): complement is 3. `3 in seen` is True!
  It matches index 0. Returns `[0, 1]`!
By checking BEFORE adding to the dictionary, an element can NEVER pair with itself!

---
Comparison of Approaches:
| Approach | Time Complexity | Space Complexity | Interview Verdict |
| :--- | :--- | :--- | :--- |
| **1. Brute Force (Nested Loops)** | O(n^2) | O(1) | Sub-optimal |
| **2. Sort + Two Pointers** | O(n log n) | O(n) | Good, but not optimal |
| **3. Single-Pass Hash Map** | **O(n)** | **O(n)** | ✅ **Optimal Gold Standard** |

---
Complexity Analysis:
- Time Complexity: O(n) — We traverse the list containing n elements only once.
  Each lookup and insertion in the hash map takes O(1) average time.
- Space Complexity: O(n) — In the worst case, the hash map stores up to n elements.
"""

from typing import List


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Approach 1: Brute force checking all pairs.
    Time: O(n^2), Space: O(1).
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Approach 3: Optimal single-pass hash map complement lookup.
    Time: O(n), Space: O(n).
    
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.
        
    Returns:
        List[int]: Indices of the two numbers adding to target.
    """
    seen = {}  # {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement has already been encountered
        if complement in seen:
            return [seen[complement], i]
            
        # Store current number and its index
        seen[num] = i
        
    return []


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard case", [2, 7, 11, 15], 9, [0, 1]),
        ("Numbers not at start", [3, 2, 4], 6, [1, 2]),
        ("Duplicate elements equal target", [3, 3], 6, [0, 1]),
        ("Negative numbers in array", [-3, 4, 3, 90], 0, [0, 2]),
        ("All negative numbers", [-10, -5, -2, -8], -15, [0, 1]),
        ("Large numbers", [1000000, 500, 2000000], 3000000, [0, 2]),
        ("Target at very end of array", [1, 5, 8, 12, 19], 31, [3, 4]),
    ]

    print("Running Tests for Problem 026: Two Sum\n" + "-" * 70)
    all_passed = True
    for name, nums, target, expected in test_cases:
        res_brute = two_sum_brute_force(nums, target)
        res_opt = two_sum(nums, target)
        
        passed = (sorted(res_opt) == sorted(expected))
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:32} | Target: {str(target):7} | Result: {res_opt} (Expected: {expected})")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! Phase 3 Started! ")
