"""
Problem 011: First Non-Repeating Character in a String
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy (LeetCode 387 - Top Interview Classic)
Core Concept: Hash Map / Frequency Counting / Two-Pass Linear Scan

---
Problem Statement:
Given a string `s`, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Example 1:
    Input: s = "leetcode"
    Output: 0
    Explanation: 'l' is the first unique character and appears at index 0.

Example 2:
    Input: s = "loveleetcode"
    Output: 2
    Explanation: 'v' appears at index 2 with frequency 1.

Example 3:
    Input: s = "aabb"
    Output: -1
    Explanation: Every character repeats.
---

Intuition (Real-World Analogy: Guest Arrival & Roll Call 📋):
Imagine people entering a hall and signing a guestbook:
- Pass 1 (Tallying):
  Count how many times each letter appears in the string.
  For "leetcode":
      {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}
- Pass 2 (Roll Call in Order):
  Walk through the string from left to right:
  - Check 'l' (index 0) -> Count is 1! We found our winner immediately! Return 0.
- If we finish the entire string without finding any count of 1, return -1.

---
Beginner Trap Alert ⚠️:
Never use `s.count(ch)` inside a loop!
```python
# ❌ DANGEROUS O(n^2) CODE:
for i, ch in enumerate(s):
    if s.count(ch) == 1:  # s.count() scans the entire string O(n)!
        return i
```
Because `s.count(ch)` is O(n), running it inside an O(n) loop turns your algorithm into O(n^2),
causing Time Limit Exceeded (TLE) on large strings!

---
Complexity Analysis:
- Time Complexity: O(n) — Pass 1 takes O(n) to count frequencies, Pass 2 takes O(n) to find the first unique.
- Space Complexity: O(1) or O(Σ) — The hash map stores at most 26 lowercase English letters, which is constant space.
"""

from typing import Dict
from collections import Counter


def first_unique_char_dict(s: str) -> int:
    """
    Finds index of the first non-repeating character using a standard hash map.
    """
    # Pass 1: Build frequency map
    freq: Dict[str, int] = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        
    # Pass 2: Find the first character with frequency 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
            
    return -1


def first_unique_char_counter(s: str) -> int:
    """
    Pythonic variation using collections.Counter.
    """
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Unique at first index", "leetcode", 0),
        ("Unique in middle", "loveleetcode", 2),
        ("No unique characters", "aabb", -1),
        ("Single character string", "z", 0),
        ("Unique at the very end", "aabbc", 4),
        ("All identical characters", "aaaaaa", -1),
        ("Empty string", "", -1),
    ]

    print("Running Tests for Problem 011: First Non-Repeating Character\n" + "-" * 70)
    all_passed = True
    for name, s, expected in test_cases:
        res_dict = first_unique_char_dict(s)
        res_counter = first_unique_char_counter(s)
        
        passed = (res_dict == expected) and (res_counter == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        char_found = s[res_dict] if res_dict != -1 else "None"
        print(f"[{status}] {name:26} | Input: {s:14} | Index: {res_dict:2} (Char: '{char_found}')")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
