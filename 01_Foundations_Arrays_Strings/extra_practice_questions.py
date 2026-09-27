"""
Phase 1: Extra Practice Questions (16 Curated Interview Problems)
Folder: 01_Foundations_Arrays_Strings

Instructions:
-------------
1. Each function below has a docstring with problem description, examples, and constraints.
2. Replace `# TODO: Write your code here` with your implementation.
3. Run this file in your terminal:
       python 01_Foundations_Arrays_Strings/extra_practice_questions.py
4. Watch each question turn from [PENDING 🟡] to [PASSED 🟢]!
"""

from typing import List, Dict, Set
from collections import Counter


# =====================================================================
# Question 1: Running Sum of 1D Array (LeetCode 1480)
# =====================================================================
def running_sum(nums: List[int]) -> List[int]:
    """
    Given an array nums, return the running sum where runningSum[i] = sum(nums[0]...nums[i]).
    
    Example:
        Input: nums = [1, 2, 3, 4]
        Output: [1, 3, 6, 10]
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 2: Maximum Consecutive Ones (LeetCode 485)
# =====================================================================
def find_max_consecutive_ones(nums: List[int]) -> int:
    """
    Given a binary array nums, return the maximum number of consecutive 1's in the array.
    
    Example:
        Input: nums = [1, 1, 0, 1, 1, 1]
        Output: 3
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 3: Squares of a Sorted Array (LeetCode 977)
# =====================================================================
def sorted_squares(nums: List[int]) -> List[int]:
    """
    Given an integer array nums sorted in non-decreasing order, return an array
    of the squares of each number sorted in non-decreasing order.
    Target: O(n) time using Two Pointers!
    
    Example:
        Input: nums = [-4, -1, 0, 3, 10]
        Output: [0, 1, 9, 16, 100]
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 4: Merge Sorted Array in Place (LeetCode 88)
# =====================================================================
def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    """
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order.
    nums1 has a length of m + n, where the first m elements are valid, and the last n are 0s.
    Merge nums2 into nums1 as one sorted array in-place.
    
    Example:
        Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
        Output: [1, 2, 2, 3, 5, 6]
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 5: Find Pivot Index (LeetCode 724)
# =====================================================================
def pivot_index(nums: List[int]) -> int:
    """
    Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all numbers strictly to the left
    of the index is equal to the sum of all numbers strictly to the right.
    Return the leftmost pivot index. If no such index exists, return -1.
    
    Example:
        Input: nums = [1, 7, 3, 6, 5, 6]
        Output: 3 (left sum = 1+7+3 = 11, right sum = 5+6 = 11)
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 6: Majority Element (> n/2 times) (LeetCode 169)
# =====================================================================
def majority_element(nums: List[int]) -> int:
    """
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    
    Example:
        Input: nums = [2, 2, 1, 1, 1, 2, 2]
        Output: 2
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 7: Contains Duplicate (LeetCode 217)
# =====================================================================
def contains_duplicate(nums: List[int]) -> bool:
    """
    Given an integer array nums, return True if any value appears at least twice,
    and return False if every element is distinct.
    
    Example:
        Input: nums = [1, 2, 3, 1]
        Output: True
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 8: Single Number (LeetCode 136)
# =====================================================================
def single_number(nums: List[int]) -> int:
    """
    Given a non-empty array of integers nums, every element appears twice except for one.
    Find that single one.
    Requirement: O(n) time and O(1) space using Bitwise XOR!
    
    Example:
        Input: nums = [4, 1, 2, 1, 2]
        Output: 4
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 9: Is Subsequence (LeetCode 392)
# =====================================================================
def is_subsequence(s: str, t: str) -> bool:
    """
    Given two strings s and t, return True if s is a subsequence of t, or False otherwise.
    (A subsequence is formed by deleting some/no characters without disturbing relative order).
    
    Example:
        Input: s = "abc", t = "ahbgdc"
        Output: True
        
        Input: s = "axc", t = "ahbgdc"
        Output: False
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 10: Length of Last Word (LeetCode 58)
# =====================================================================
def length_of_last_word(s: str) -> int:
    """
    Given a string s consisting of words and spaces, return the length of the last word in the string.
    
    Example:
        Input: s = "   fly me   to   the moon  "
        Output: 4 ("moon")
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 11: Valid Palindrome II (LeetCode 680)
# =====================================================================
def valid_palindrome_ii(s: str) -> bool:
    """
    Given a string s, return True if the s can be a palindrome after deleting
    at most one character from it.
    
    Example:
        Input: s = "aba" -> Output: True
        Input: s = "abca" -> Output: True (delete 'c')
        Input: s = "abc" -> Output: False
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 12: Jewels and Stones (LeetCode 771)
# =====================================================================
def num_jewels_in_stones(jewels: str, stones: str) -> int:
    """
    You're given strings jewels representing the types of stones that are jewels,
    and stones representing the stones you have.
    How many of the stones you have are also jewels?
    
    Example:
        Input: jewels = "aA", stones = "aAAbbbb"
        Output: 3
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 13: Ransom Note (LeetCode 383)
# =====================================================================
def can_construct_ransom_note(ransomNote: str, magazine: str) -> bool:
    """
    Given two strings ransomNote and magazine, return True if ransomNote can be
    constructed by using the letters from magazine and False otherwise.
    Each letter in magazine can only be used once.
    
    Example:
        Input: ransomNote = "aa", magazine = "aab"
        Output: True
        
        Input: ransomNote = "aa", magazine = "ab"
        Output: False
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 14: Maximum Product of Two Elements in Array (LeetCode 1464)
# =====================================================================
def max_product(nums: List[int]) -> int:
    """
    Given the array of integers nums, choose two different indices i and j.
    Return the maximum value of (nums[i]-1)*(nums[j]-1).
    Target: O(n) single pass tracking the two largest numbers!
    
    Example:
        Input: nums = [3, 4, 5, 2]
        Output: 12 (since (5-1)*(4-1) = 4*3 = 12)
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 15: Left and Right Sum Differences (LeetCode 2574)
# =====================================================================
def left_right_difference(nums: List[int]) -> List[int]:
    """
    Given an integer array nums, return an array answer where:
    answer[i] = |leftSum[i] - rightSum[i]|.
    
    Example:
        Input: nums = [10, 4, 8, 3]
        Output: [15, 1, 11, 22]
        Explanation: leftSum = [0, 10, 14, 22], rightSum = [15, 11, 3, 0]
                     difference = [|0-15|, |10-11|, |14-3|, |22-0|] = [15, 1, 11, 22]
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Question 16: Count Number of Pairs with Absolute Difference K (LeetCode 2006)
# =====================================================================
def count_k_difference(nums: List[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, return the number of pairs (i, j)
    where i < j such that |nums[i] - nums[j]| == k.
    Target: O(n) using a Hash Map / Frequency Counter!
    
    Example:
        Input: nums = [1, 2, 2, 1], k = 1
        Output: 4
    """
    # TODO: Write your code here
    raise NotImplementedError("Write your solution here!")


# =====================================================================
# Test Suite Runner
# =====================================================================
if __name__ == "__main__":
    tests = [
        ("Q01: Running Sum of 1D Array", running_sum, ([1, 2, 3, 4],), [1, 3, 6, 10]),
        ("Q02: Max Consecutive Ones", find_max_consecutive_ones, ([1, 1, 0, 1, 1, 1],), 3),
        ("Q03: Squares of a Sorted Array", sorted_squares, ([-4, -1, 0, 3, 10],), [0, 1, 9, 16, 100]),
        ("Q04: Merge Sorted Array", lambda: merge_sorted_arrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), (), [1, 2, 2, 3, 5, 6]),
        ("Q05: Find Pivot Index", pivot_index, ([1, 7, 3, 6, 5, 6],), 3),
        ("Q06: Majority Element", majority_element, ([2, 2, 1, 1, 1, 2, 2],), 2),
        ("Q07: Contains Duplicate", contains_duplicate, ([1, 2, 3, 1],), True),
        ("Q08: Single Number", single_number, ([4, 1, 2, 1, 2],), 4),
        ("Q09: Is Subsequence", is_subsequence, ("abc", "ahbgdc"), True),
        ("Q10: Length of Last Word", length_of_last_word, ("   fly me   to   the moon  ",), 4),
        ("Q11: Valid Palindrome II", valid_palindrome_ii, ("abca",), True),
        ("Q12: Jewels and Stones", num_jewels_in_stones, ("aA", "aAAbbbb"), 3),
        ("Q13: Ransom Note", can_construct_ransom_note, ("aa", "aab"), True),
        ("Q14: Max Product of Two Elements", max_product, ([3, 4, 5, 2],), 12),
        ("Q15: Left and Right Sum Differences", left_right_difference, ([10, 4, 8, 3],), [15, 1, 11, 22]),
        ("Q16: Count K-Difference Pairs", count_k_difference, ([1, 2, 2, 1], 1), 4),
    ]

    print("=" * 75)
    print("  Phase 1: Extra Practice Test Workbench (16 Questions)")
    print("=" * 75)
    
    passed_count = 0
    pending_count = 0
    failed_count = 0
    
    for title, func, args, expected in tests:
        try:
            actual = func(*args)
            if actual == expected:
                print(f"[PASSED]  {title:45}")
                passed_count += 1
            else:
                print(f"[FAILED]  {title:45} | Output: {actual} (Expected: {expected})")
                failed_count += 1
        except NotImplementedError:
            print(f"[PENDING] {title:45} | (Write your code here)")
            pending_count += 1
        except Exception as e:
            print(f"[ERROR]   {title:45} | Exception: {e}")
            failed_count += 1
            
    print("=" * 75)
    print(f"Summary: {passed_count} Passed | {pending_count} Pending | {failed_count} Failed")
    print("=" * 75)
