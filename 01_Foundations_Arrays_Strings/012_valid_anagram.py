"""
Problem 012: Valid Anagram
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy (LeetCode 242 - Top Interview Classic)
Core Concept: Hashing / Frequency Counting / Fixed-Size Frequency Array

---
Problem Statement:
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: True

Example 2:
    Input: s = "rat", t = "car"
    Output: False

Example 3:
    Input: s = "a", t = "ab"
    Output: False
---

Intuition & Approaches:

1. Approach 1: Sorting 🔤
   - If two words are anagrams, their sorted versions must be IDENTICAL:
     `sorted(s) == sorted(t)`
   - Time: O(n log n)
   - Space: O(n) auxiliary space for sorted characters.

2. Approach 2: Two Frequency Maps (Counter) 📊
   - Count character frequencies for both strings:
     `Counter(s) == Counter(t)`
   - Time: O(n)
   - Space: O(1) for English alphabet (max 26 entries).

3. Approach 3: Single Fixed Array / Incrementation-Decrementation (Optimal! ⚡)
   - If `len(s) != len(t)`, they CANNOT be anagrams -> return False immediately!
   - Use a single frequency array of size 26 (or a dict for Unicode).
   - For each character in `s`: count += 1.
   - For each character in `t`: count -= 1.
   - If all counts end up at 0, they are exact anagrams!

---
Recruiter Follow-Up 🔥:
"What if the inputs contain Unicode characters (e.g., emojis, accents, non-English scripts)?"
Answer: An array of size 26 only works for lowercase English [a-z].
For general Unicode, use a Python `dict` or `collections.Counter`, which handles all
Unicode code points seamlessly!

---
Complexity Analysis:
- Time Complexity: O(n) — Single pass over strings of length n.
- Space Complexity: O(1) — At most 26 lowercase English letters in the map.
"""

from collections import Counter
from typing import Dict


def is_anagram_sorting(s: str, t: str) -> bool:
    """
    Approach 1: Sorting based comparison.
    Time: O(n log n), Space: O(n).
    """
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def is_anagram_counter(s: str, t: str) -> bool:
    """
    Approach 2: Pythonic frequency comparison using collections.Counter.
    Time: O(n), Space: O(1).
    """
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


def is_anagram_optimal(s: str, t: str) -> bool:
    """
    Approach 3: Single frequency map with increment-decrement counting.
    Optimal, generalizable to Unicode, handles early termination.
    Time: O(n), Space: O(1).
    """
    if len(s) != len(t):
        return False
        
    counts: Dict[str, int] = {}
    
    # Increment for s, decrement for t
    for char_s, char_t in zip(s, t):
        counts[char_s] = counts.get(char_s, 0) + 1
        counts[char_t] = counts.get(char_t, 0) - 1
        
    # Check if all counts balanced out to 0
    return all(val == 0 for val in counts.values())


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Valid anagram", "anagram", "nagaram", True),
        ("Different characters", "rat", "car", False),
        ("Different lengths", "a", "ab", False),
        ("Single identical char", "a", "a", True),
        ("Same characters different frequencies", "aa", "a", False),
        ("Longer valid anagram", "listen", "silent", True),
        ("Unicode characters", "café", "féca", True),
        ("Empty strings", "", "", True),
    ]

    print("Running Tests for Problem 012: Valid Anagram\n" + "-" * 70)
    all_passed = True
    for name, s, t, expected in test_cases:
        res_sort = is_anagram_sorting(s, t)
        res_counter = is_anagram_counter(s, t)
        res_opt = is_anagram_optimal(s, t)
        
        passed = (res_sort == expected) and (res_counter == expected) and (res_opt == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:38} | ('{s}', '{t}') -> {res_opt}")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! Day 3 Complete (12/100)!")
