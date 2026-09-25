"""
Problem 009: Find the Duplicate Number
Phase: 01_Foundations_Arrays_Strings
Difficulty: Medium (LeetCode 287 - Top Interview / FAANG Classic)
Core Concept: Hashing / Hash Set / Floyd's Tortoise and Hare (Cycle Detection)

---
Problem Statement:
Given an array of integers `nums` containing `n + 1` integers where each integer
is in the range `[1, n]` inclusive.
There is only one repeated number in `nums`, return this repeated number.

Example 1:
    Input: nums = [1, 3, 4, 2, 2]
    Output: 2

Example 2:
    Input: nums = [3, 1, 3, 4, 2]
    Output: 3

Example 3:
    Input: nums = [3, 3, 3, 3, 3]
    Output: 3

---
Recruiter Constraints (The FAANG Challenge 🏆):
1. You must not modify the array (read-only).
2. You must use only constant O(1) extra space.
3. Runtime complexity must be less than O(n^2), ideally O(n).

---
Approach 1: Hash Set (The Intuitive Foundation 🧠)
- Keep a `seen = set()`.
- As you iterate, check if `num in seen`.
- If yes, you found the duplicate! If no, `seen.add(num)`.
- Time Complexity: O(n)
- Space Complexity: O(n) — Stores up to n elements in the set.
(Good start, but fails the O(1) space constraint!)

---
Approach 2: Floyd's Tortoise and Hare Algorithm (Optimal O(1) Space 🐢🐇)
Why can an array be treated as a Linked List?
- Every value `nums[i]` is in the range `[1, n]`.
- This means every value points to a valid index in the array: `current -> nums[current]`.
- Since there are `n + 1` elements and values are between `1` and `n`, by Pigeonhole Principle,
  at least two different indices point to the SAME next node.
- Two nodes pointing to the same node creates a CYCLE!
- The entrance to the cycle is the duplicate number!

Two-Phase Algorithm:
Phase 1 (Detect Intersection):
    slow = nums[0]
    fast = nums[0]
    slow moves 1 step: slow = nums[slow]
    fast moves 2 steps: fast = nums[nums[fast]]
    Keep going until slow == fast.

Phase 2 (Find Cycle Entrance):
    Reset slow = nums[0] (or 0)
    Move both slow and fast 1 step at a time:
        slow = nums[slow]
        fast = nums[fast]
    The node where they meet is the DUPLICATE number!

- Time Complexity: O(n)
- Space Complexity: O(1) — Strictly constant space without modifying input!
"""

from typing import List


def find_duplicate_hashset(nums: List[int]) -> int:
    """
    Finds the duplicate number using a Hash Set.
    Time: O(n), Space: O(n).
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1


def find_duplicate_floyd(nums: List[int]) -> int:
    """
    Finds the duplicate number using Floyd's Cycle Detection Algorithm (Tortoise & Hare).
    Satisfies FAANG constraints: O(n) time, O(1) space, Read-only array.
    """
    # Phase 1: Finding the intersection point in the cycle
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]           # 1 step
        fast = nums[nums[fast]]     # 2 steps
        if slow == fast:
            break
            
    # Phase 2: Finding the entrance to the cycle (the duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]           # 1 step
        fast = nums[fast]           # 1 step
        
    return slow


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Duplicate at end", [1, 3, 4, 2, 2], 2),
        ("Duplicate in middle", [3, 1, 3, 4, 2], 3),
        ("All identical values", [3, 3, 3, 3, 3], 3),
        ("Two elements with duplicate", [1, 1], 1),
        ("Duplicate at beginning", [2, 2, 2, 2, 1], 2),
        ("Unordered cycle", [2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9),
    ]

    print("Running Tests for Problem 009: Find the Duplicate Number\n" + "-" * 70)
    all_passed = True
    for name, nums, expected in test_cases:
        res_set = find_duplicate_hashset(nums)
        res_floyd = find_duplicate_floyd(nums)
        
        passed = (res_set == expected) and (res_floyd == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:28} | HashSet: {res_set} | Floyd: {res_floyd} | Expected: {expected}")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
