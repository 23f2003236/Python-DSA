"""
Problem 010: Frequency of Elements in an Array
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy
Core Concept: Hash Map / Dictionary / Frequency Counting / collections.Counter

---
Problem Statement:
Given an array of elements (integers or strings), count the frequency of each
distinct element and return the frequency map.
Also provide methods to:
1. Query the frequency of any element in O(1) time.
2. Find the most frequent element (the Mode) in the array.

Example 1:
    Input: nums = [1, 2, 2, 3, 3, 3, 4]
    Output: {1: 1, 2: 2, 3: 3, 4: 1}
    Most Frequent: 3 (frequency: 3)

Example 2:
    Input: words = ["apple", "banana", "apple", "cherry", "apple", "banana"]
    Output: {"apple": 3, "banana": 2, "cherry": 1}
    Most Frequent: "apple" (frequency: 3)
---

Intuition (Real-World Analogy: Tally Marks in an Election 🗳️):
Imagine you are opening an election ballot box:
- You have a notepad (the Hash Map / Dictionary).
- For each vote you pull out:
  - If the candidate is already in your notepad: add +1 to their tally mark.
  - If it's the first time you see this candidate: write their name with tally 1.
- Hash Maps provide O(1) average lookup and insertion, meaning each vote takes constant time!

---
Three Pythonic Ways to Build a Frequency Map:
1. Standard `dict` with `dict.get(key, 0) + 1`
   - Universal logic that transfers directly to Java (HashMap), C++ (unordered_map), etc.
2. `collections.defaultdict(int)`
   - Avoids `KeyError` automatically; clean and readable.
3. `collections.Counter(nums)`
   - Python's standard high-performance tool for frequency counting.

---
Complexity Analysis:
- Time Complexity: O(n) — We traverse the array of n elements once.
- Space Complexity: O(k) — Where k is the number of unique elements (k <= n).
- Lookup Time: O(1) average for any subsequent frequency query.
"""

from typing import List, Dict, Tuple, Any
from collections import defaultdict, Counter


def count_frequency_dict(nums: List[Any]) -> Dict[Any, int]:
    """
    Builds a frequency dictionary using standard dict and .get().
    Universal approach across all programming languages.
    """
    freq = {}
    for item in nums:
        freq[item] = freq.get(item, 0) + 1
    return freq


def count_frequency_defaultdict(nums: List[Any]) -> Dict[Any, int]:
    """
    Builds a frequency dictionary using collections.defaultdict.
    """
    freq = defaultdict(int)
    for item in nums:
        freq[item] += 1
    return dict(freq)


def count_frequency_counter(nums: List[Any]) -> Counter:
    """
    Builds a frequency map using Python's optimized collections.Counter.
    """
    return Counter(nums)


def get_most_frequent_element(nums: List[Any]) -> Tuple[Any, int]:
    """
    Returns the element with the highest frequency and its count.
    If multiple elements tie, returns any one of the champions.
    """
    if not nums:
        return (None, 0)
        
    freq_map = count_frequency_dict(nums)
    
    max_item = None
    max_count = -1
    
    for item, count in freq_map.items():
        if count > max_count:
            max_count = count
            max_item = item
            
    return (max_item, max_count)


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Integers with varying frequencies", [1, 2, 2, 3, 3, 3, 4], {1: 1, 2: 2, 3: 3, 4: 1}, (3, 3)),
        ("All unique numbers", [10, 20, 30], {10: 1, 20: 1, 30: 1}, (10, 1)),
        ("All identical numbers", [5, 5, 5, 5], {5: 4}, (5, 4)),
        ("String words list", ["cat", "dog", "cat", "bird", "dog", "cat"], {"cat": 3, "dog": 2, "bird": 1}, ("cat", 3)),
        ("Negative numbers", [-1, -2, -1, -3, -1], {-1: 3, -2: 1, -3: 1}, (-1, 3)),
        ("Empty list", [], {}, (None, 0)),
    ]

    print("Running Tests for Problem 010: Frequency of Elements in Array\n" + "-" * 75)
    all_passed = True
    for name, input_data, expected_map, (exp_item, exp_freq) in test_cases:
        dict_res = count_frequency_dict(input_data)
        default_res = count_frequency_defaultdict(input_data)
        counter_res = count_frequency_counter(input_data)
        most_freq_item, most_freq_count = get_most_frequent_element(input_data)
        
        map_passed = (dict_res == expected_map) and (default_res == expected_map) and (dict(counter_res) == expected_map)
        mode_passed = (most_freq_count == exp_freq)
        
        passed = map_passed and mode_passed
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:33} | Unique Items: {len(dict_res):2} | Most Frequent: {most_freq_item} (Count: {most_freq_count})")
        
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! ")
