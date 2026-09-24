"""
Problem 003: Find Second Largest Element in an Array (Distinct)
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy-Medium
Core Concept: Invariant Tracking / Single Pass Multi-variable State

---
Problem Statement:
Given an array (list) of integers, find and return the second largest DISTINCT element.
If no second largest distinct element exists (e.g., fewer than 2 elements, or all elements are identical),
return None (or -1 depending on platform convention).

Example 1:
    Input: nums = [12, 35, 1, 10, 34, 1]
    Output: 34

Example 2 (Duplicates of largest):
    Input: nums = [10, 10, 10, 9]
    Output: 9 (10 is the largest, 9 is the 2nd largest distinct)

Example 3 (All identical):
    Input: nums = [5, 5, 5]
    Output: None

Example 4 (Negative numbers):
    Input: nums = [-10, -5, -20, -2]
    Output: -5 (-2 is largest, -5 is second largest)
---

Intuition (Real-World Analogy: Gold & Silver Medals):
Imagine you are managing an athletic race and giving out Gold and Silver medals:
- `first` is your Gold Medalist.
- `second` is your Silver Medalist.

When a new runner crosses the finish line with score `num`:
1. Case 1: `num > first`
   The new runner just beat your Gold medalist!
   - The former Gold medalist gets demoted to Silver: `second = first`
   - The new runner takes the Gold: `first = num`
2. Case 2: `num < first` but `num > second`
   The new runner didn't beat Gold, but beat your Silver medalist!
   - The new runner takes the Silver: `second = num`
3. Case 3: `num == first`
   A duplicate of the Gold medalist arrived. Ignore them because we only want
   DISTINCT rankings!
4. Case 4: `num <= second`
   They didn't beat Silver. Ignore.

---
Comparison of Approaches:
| Approach | Time | Space | Notes |
| :--- | :--- | :--- | :--- |
| 1. Sort Unique (`sorted(set(nums))[-2]`) | O(n log n) | O(n) | Slow, extra memory. |
| 2. Two Passes (1st pass max, 2nd pass 2nd max) | O(n) + O(n) = O(n) | O(1) | Works, but requires two full iterations. |
| 3. Single Pass (Gold/Silver logic) | O(n) | O(1) | **Optimal & expected by recruiters.** |

---
Complexity Analysis:
- Time Complexity: O(n) — Single pass through the array.
- Space Complexity: O(1) — Only two variables (`first`, `second`) used.
"""

from typing import List, Optional


def find_second_largest(nums: List[int]) -> Optional[int]:
    """
    Finds the second largest distinct integer in nums using an optimal single pass.
    
    Args:
        nums (List[int]): List of integers.
        
    Returns:
        Optional[int]: The second largest distinct integer, or None if it doesn't exist.
    """
    # Base Case: Must have at least 2 elements
    if not nums or len(nums) < 2:
        return None
    
    # Initialize both champions to negative infinity
    first = float('-inf')
    second = float('-inf')
    
    for num in nums:
        # Case 1: New absolute champion found
        if num > first:
            second = first    # Former first drops to second
            first = num       # Update first
        # Case 2: Beats second, but strictly smaller than first (ensures distinct)
        elif num > second and num != first:
            second = num
            
    # If second was never updated from negative infinity, no distinct second exists
    return int(second) if second != float('-inf') else None


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard unsorted array", [12, 35, 1, 10, 34, 1], 34),
        ("Duplicates of max element", [10, 10, 10, 9], 9),
        ("All identical elements", [5, 5, 5, 5], None),
        ("All negative numbers", [-10, -5, -20, -2], -5),
        ("Two elements descending", [10, 5], 5),
        ("Two elements ascending", [5, 10], 5),
        ("Single element", [100], None),
        ("Empty list", [], None),
        ("Already sorted ascending", [1, 2, 3, 4, 5], 4),
        ("Already sorted descending", [5, 4, 3, 2, 1], 4),
    ]

    print("Running Tests for Problem 003: Find Second Largest Element\n" + "-" * 65)
    all_passed = True
    for name, nums, expected in test_cases:
        actual = find_second_largest(nums)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:27} | Input: {str(nums):24} | Result: {str(actual):6} (Expected: {expected})")
        
    print("-" * 65)
    if all_passed:
        print("All test cases passed successfully!")
