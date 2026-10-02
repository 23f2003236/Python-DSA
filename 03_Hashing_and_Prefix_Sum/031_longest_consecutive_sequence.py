"""
Problem 031: Longest Consecutive Sequence
Phase: 03_Hashing_and_Prefix_Sum
Difficulty: Medium (LeetCode 128 - Top Interview 150 Classic)
Core Concept: Hash Set / The Streak Starter Pattern / Amortized O(n) Time

---
Problem Statement:
Given an unsorted array of integers `nums`, return the length of the longest
consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Its length is 4.

Example 2:
    Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9
    Explanation: The sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Length is 9.

Example 3:
    Input: nums = []
    Output: 0
---

Intuition (The Streak Starter Pattern 🚀):
Why NOT sorting?
- Sorting takes O(n log n) time, which violates the strict O(n) constraint!

How to do it in O(n) using a Hash Set?
1. Convert `nums` into a Hash Set: `num_set = set(nums)`.
   Sets provide O(1) average lookup.
2. For each number `x` in `num_set`:
   Ask: "Is `x` the START of a consecutive sequence?"
   - If `(x - 1) in num_set`:
     NO! `x` is in the middle of someone else's streak. Skip it immediately!
   - If `(x - 1) not in num_set`:
     YES! `x` is a genuine **Streak Starter**!
     From `x`, count upwards: `x + 1`, `x + 2`, `x + 3`... as long as they exist in `num_set`.
     Record the length of this streak.
3. Update `max_streak = max(max_streak, current_streak)`.

---
Why is this strictly O(n) time? (Amortized Analysis) ⏱️
At first glance, a while loop inside a for loop looks like O(n^2).
However:
- The while loop ONLY executes for numbers that are Streak Starters.
- Every number in a sequence is checked as a streak starter once, and visited in the while loop once.
- Total visits per number = at most 2 times!
- Overall Time Complexity = O(n)!

---
Complexity Analysis:
- Time Complexity: O(n) — Inserting into set takes O(n), and scanning sequences visits each number at most twice.
- Space Complexity: O(n) — Hash set stores up to n elements.
"""

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Finds the length of the longest consecutive sequence in O(n) time using a Hash Set.
    
    Args:
        nums (List[int]): Unsorted list of integers.
        
    Returns:
        int: Length of the longest consecutive elements sequence.
    """
    if not nums:
        return 0
        
    num_set = set(nums)
    max_streak = 0
    
    for num in num_set:
        # Check if 'num' is the start of a sequence (i.e. num - 1 is NOT in set)
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            
            # Count the length of the streak forward
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
                
            max_streak = max(max_streak, current_streak)
            
    return max_streak


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard unsorted array", [100, 4, 200, 1, 3, 2], 4),
        ("Longer sequence with zeros", [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ("Duplicates in array", [1, 2, 0, 1], 3),
        ("Negative numbers sequence", [-5, -4, -3, 0, 2, 3], 3),
        ("Disjoint single elements", [10, 30, 50, 70], 1),
        ("All identical elements", [7, 7, 7, 7], 1),
        ("Single element array", [42], 1),
        ("Empty array", [], 0),
    ]

    print("Running Tests for Problem 031: Longest Consecutive Sequence\n" + "-" * 75)
    all_passed = True
    for name, nums, expected in test_cases:
        actual = longest_consecutive(nums)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:32} | Input: {str(nums):25} | Length: {actual} (Exp: {expected})")
        
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! ")
