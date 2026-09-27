"""
Problem 013: Valid Palindrome String
Phase: 01_Foundations_Arrays_Strings
Difficulty: Easy (LeetCode 125 - Top Interview Classic)
Core Concept: Two Pointers / String Manipulation / In-place Character Comparison

---
Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward
and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return True if it is a palindrome, or False otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: False
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: True
    Explanation: s is an empty string "" after removing non-alphanumerics, which reads the same backward and forward.
---

Intuition (Real-World Analogy: Two Pointers Inward Scan ↔️):
Imagine two fingers pointing at the start and end of a sentence:
1. `left` starts at 0, `right` starts at len(s) - 1.
2. If `s[left]` is not alphanumeric (space, comma, colon, etc.):
   Skip it and move `left += 1`.
3. If `s[right]` is not alphanumeric:
   Skip it and move `right -= 1`.
4. Once both point to valid alphanumeric characters:
   Compare their lowercase versions:
   - If `s[left].lower() != s[right].lower()`: return False immediately (Early Exit)!
   - If they match: move both inward (`left += 1`, `right -= 1`).
5. When `left >= right`, all pairs matched — return True!

---
Why Two Pointers (O(1) Space) Beats Filter & Reverse (O(n) Space):
- Approach 1 (Filter + Slicing):
  `clean = [c.lower() for c in s if c.isalnum()]`
  `return clean == clean[::-1]`
  Creates two new lists in memory -> O(n) extra space.
- Approach 2 (Two Pointers In-Place):
  No extra strings or lists created -> O(1) space!

---
Complexity Analysis:
- Time Complexity: O(n) — Each character is visited at most twice by left and right pointers.
- Space Complexity: O(1) — Strictly constant space; no extra copies created.
"""


def is_palindrome_filtering(s: str) -> bool:
    """
    Approach 1: Filter alphanumeric characters and compare with reverse.
    Time: O(n), Space: O(n).
    """
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return filtered == filtered[::-1]


def is_palindrome_two_pointers(s: str) -> bool:
    """
    Approach 2: Two pointers moving inward with character skipping.
    Optimal: Time O(n), Space O(1).
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Move left pointer forward if not alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
            
        # Move right pointer backward if not alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Compare characters case-insensitively
        if s[left].lower() != s[right].lower():
            return False  # Early exit
            
        left += 1
        right -= 1
        
    return True


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Classic Panama palindrome", "A man, a plan, a canal: Panama", True),
        ("Sentence not palindrome", "race a car", False),
        ("Punctuation and spaces only", "   , . : ; ! ", True),
        ("Single character", "a", True),
        ("Alphanumeric with numbers", "0P0", True),
        ("Alphanumeric mismatch with numbers", "0P", False),
        ("Already symmetric word", "madam", True),
        ("Empty string", "", True),
    ]

    print("Running Tests for Problem 013: Valid Palindrome String\n" + "-" * 70)
    all_passed = True
    for name, s, expected in test_cases:
        res_filter = is_palindrome_filtering(s)
        res_pointers = is_palindrome_two_pointers(s)
        
        passed = (res_filter == expected) and (res_pointers == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:35} | Result: {res_pointers} (Expected: {expected})")
        
    print("-" * 70)
    if all_passed:
        print("All test cases passed successfully! ")
