"""
Problem 015: Rotate Array by K Steps
Phase: 01_Foundations_Arrays_Strings
Difficulty: Medium (LeetCode 189 - Top Interview Classic)
Core Concept: Array Reversal Algorithm / In-place Array Mutation / Modulo Arithmetic

---
Problem Statement:
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.
You must do this IN-PLACE with O(1) extra space.

Example 1:
    Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [5, 6, 7, 1, 2, 3, 4]
    Explanation:
    rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
    rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
    rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]

Example 2:
    Input: nums = [-1, -100, 3, 99], k = 2
    Output: [3, 99, -1, -100]

Example 3 (k greater than array length):
    Input: nums = [1, 2], k = 5
    Output: [2, 1] (Since 5 % 2 = 1 step rotation)
---

Intuition (The 3-Step Reversal Magic 🪄):
Suppose nums = [1, 2, 3, 4, 5, 6, 7] and k = 3.
Notice that the last k elements [5, 6, 7] move to the front, and the first n-k elements [1, 2, 3, 4] move to the back!

How can we achieve this in-place without any extra memory?
1. Normalize k: `k = k % n` (Rotating by n brings the array back to its original state).
2. Step 1: Reverse the ENTIRE array:
   [1, 2, 3, 4, 5, 6, 7]  --->  [7, 6, 5, 4, 3, 2, 1]
3. Step 2: Reverse the FIRST k elements (from index 0 to k - 1):
   [7, 6, 5]  --->  [5, 6, 7]
   Array is now: [5, 6, 7, 4, 3, 2, 1]
4. Step 3: Reverse the REMAINING n - k elements (from index k to n - 1):
   [4, 3, 2, 1]  --->  [1, 2, 3, 4]
   Array is now: [5, 6, 7, 1, 2, 3, 4]  <-- Exactly rotated!

---
Why NOT Slicing in an Interview?
- `nums[:] = nums[-k:] + nums[:-k]` works in Python, but it allocates O(n) extra memory behind the scenes.
- Interviewers specifically want to see the 3-Step In-Place Reversal Algorithm because it works in O(1) space across any language (C++, Java, Python, Go).

---
Complexity Analysis:
- Time Complexity: O(n) — Each element is reversed at most twice.
- Space Complexity: O(1) — Strictly in-place modification.
"""

from typing import List


def rotate_array(nums: List[int], k: int) -> List[int]:
    """
    Rotates nums to the right by k steps in-place using the 3-Step Reversal Algorithm.
    
    Args:
        nums (List[int]): The array to rotate.
        k (int): Number of steps to rotate right.
        
    Returns:
        List[int]: The modified nums array.
    """
    if not nums:
        return nums
        
    n = len(nums)
    k = k % n  # Handle cases where k >= n
    
    if k == 0:
        return nums
        
    # Helper function to reverse a subarray nums[left...right] in-place
    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
    # 1. Reverse entire array
    reverse(0, n - 1)
    
    # 2. Reverse first k elements
    reverse(0, k - 1)
    
    # 3. Reverse remaining n - k elements
    reverse(k, n - 1)
    
    return nums


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard rotation", [1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ("Negative numbers rotation", [-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ("k is greater than length", [1, 2], 5, [2, 1]),
        ("k is multiple of length (no change)", [1, 2, 3], 6, [1, 2, 3]),
        ("Single element array", [42], 10, [42]),
        ("Rotate by 0 steps", [1, 2, 3, 4], 0, [1, 2, 3, 4]),
        ("Rotate by length - 1", [1, 2, 3, 4, 5], 4, [2, 3, 4, 5, 1]),
        ("Empty array", [], 3, []),
    ]

    print("Running Tests for Problem 015: Rotate Array by K Steps\n" + "-" * 75)
    all_passed = True
    for name, original, k, expected in test_cases:
        arr_copy = list(original)
        actual = rotate_array(arr_copy, k)
        passed = actual == expected
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
        print(f"[{status}] {name:32} | k={k} | Input: {str(original):20} | Result: {actual}")
        
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! ")
