"""
Problem 004: Reverse an Array (In-place Two Pointers)
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy
Core Concept: Two Pointers Technique / In-place Mutation

---
Problem Statement:
Given an array (list) of elements, reverse the array IN-PLACE (without allocating 
a new list, using O(1) extra memory).

Example 1:
    Input: nums = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

Example 2 (Even length):
    Input: nums = [10, 20, 30, 40]
    Output: [40, 30, 20, 10]

Example 3 (Single element):
    Input: nums = [42]
    Output: [42]

Example 4 (Empty list):
    Input: nums = []
    Output: []
---

Intuition (Real-World Analogy: Two People at Opposite Ends):
Imagine books arranged on a shelf in a row:
1. You place your LEFT hand on the very first book (index 0) and your RIGHT hand
   on the very last book (index n - 1).
2. Swap the two books.
3. Move your LEFT hand one step forward (`left += 1`) and your RIGHT hand one step
   backward (`right -= 1`).
4. Repeat this swap-and-move process until your hands meet or cross each other (`left >= right`).
5. The entire row is now completely reversed!

---
Why NOT `nums[::-1]` in an Interview?
- `nums[::-1]` creates an entirely NEW list in memory (O(n) auxiliary space).
- When an interviewer says "in-place", they strictly want:
  Auxiliary Space: O(1).
- Python's built-in `nums.reverse()` does this internally using the two-pointer technique.
  Implementing it manually demonstrates your foundational DSA understanding.

---
Complexity Analysis:
- Time Complexity: O(n) — We make n/2 swaps, which is asymptotically O(n).
- Space Complexity: O(1) — We modify the array directly without allocating extra memory.
"""

from typing import List


def reverse_array(nums: List[any]) -> List[any]:
    """
    Reverses a list in-place using the two pointers technique.
    
    Args:
        nums (List[any]): The list to reverse.
        
    Returns:
        List[any]: The same list reference, reversed in-place.
    """
    left = 0
    right = len(nums) - 1
    
    # Invariant: Elements before left and after right are already correctly swapped
    while left < right:
        # Swap elements at left and right pointers (Pythonic tuple unpacking)
        nums[left], nums[right] = nums[right], nums[left]
        
        # Move pointers inward towards each other
        left += 1
        right -= 1
        
    return nums


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Odd length array", [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ("Even length array", [10, 20, 30, 40], [40, 30, 20, 10]),
        ("Two elements", [1, 2], [2, 1]),
        ("Single element", [42], [42]),
        ("Empty array", [], []),
        ("Strings list", ["apple", "banana", "cherry"], ["cherry", "banana", "apple"]),
        ("Negative numbers", [-5, -2, 0, 3, 8], [8, 3, 0, -2, -5]),
        ("All identical elements", [7, 7, 7, 7], [7, 7, 7, 7]),
    ]

    print("Running Tests for Problem 004: Reverse an Array\n" + "-" * 65)
    all_passed = True
    for name, original, expected in test_cases:
        # Pass a copy to verify in-place behavior and preserve original for printing
        input_copy = list(original)
        actual = reverse_array(input_copy)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:24} | Before: {str(original):22} | After: {actual}")
        
    print("-" * 65)
    if all_passed:
        print("All test cases passed successfully! Day 1 Complete (4/4)!")
