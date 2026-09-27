"""
Problem 014: Reverse Words in a String
Phase: 01_Foundations_Arrays_Strings
Difficulty: Medium (LeetCode 151 - Top Interview Classic)
Core Concept: Two Pointers / String Parsing / Whitespace Handling

---
Problem Statement:
Given an input string `s`, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in `s` will be
separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.
Note that `s` may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
    Input: s = "the sky is blue"
    Output: "blue is sky the"

Example 2:
    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Reversed string should not contain leading or trailing spaces.

Example 3:
    Input: s = "a good   example"
    Output: "example good a"
    Explanation: Multiple spaces between words are reduced to a single space.
---

Intuition & Approaches:

1. Approach 1: The Pythonic Idiomatic Way 🐍
   `return " ".join(s.split()[::-1])`
   - How `s.split()` works in Python:
     When called without arguments, `s.split()` automatically:
     a) Trims leading and trailing whitespace.
     b) Groups consecutive whitespace into a single delimiter!
   - `[::-1]` reverses the list of words.
   - `" ".join(...)` connects them with exactly one space.
   - Time: O(n), Space: O(n).

2. Approach 2: Manual Two-Pointer Parsing (Interviewer Favorite! ⚡)
   What if an interviewer says: "Don't use built-in .split(), parse the words manually"?
   - Algorithm (Right-to-Left Traversal):
     1. Start index `i` at the end of the string (`len(s) - 1`).
     2. Skip any trailing spaces (`while i >= 0 and s[i] == ' ': i -= 1`).
     3. When a letter is found, mark the end of the word (`end = i`).
     4. Move `i` backwards until a space is found to find the start of the word (`start = i + 1`).
     5. Extract the word `s[start:end+1]` and append to our results list.
     6. Repeat until the start of the string is reached.
     7. Join the extracted words with `" "`.

---
Complexity Analysis:
- Time Complexity: O(n) — Each character in the string is visited a constant number of times.
- Space Complexity: O(n) — Required to store the parsed words and the output string (strings are immutable in Python).
"""

from typing import List


def reverse_words_pythonic(s: str) -> str:
    """
    Approach 1: Pythonic one-liner using s.split() and join.
    Time: O(n), Space: O(n).
    """
    return " ".join(s.split()[::-1])


def reverse_words_two_pointers(s: str) -> str:
    """
    Approach 2: Manual Two-Pointer parsing from right to left.
    Demonstrates manual whitespace handling and string tokenization without .split().
    Time: O(n), Space: O(n).
    """
    words: List[str] = []
    i = len(s) - 1
    
    while i >= 0:
        # Step 1: Skip any spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        if i < 0:
            break
            
        # Step 2: Mark the end of the word
        end = i
        
        # Step 3: Find the start of the word (move i until a space is hit)
        while i >= 0 and s[i] != ' ':
            i -= 1
            
        # The word spans from i + 1 to end
        word = s[i + 1 : end + 1]
        words.append(word)
        
    return " ".join(words)


# =====================================================================
# Test Cases & Verification
# =====================================================================
if __name__ == "__main__":
    test_cases = [
        ("Standard sentence", "the sky is blue", "blue is sky the"),
        ("Leading and trailing spaces", "  hello world  ", "world hello"),
        ("Multiple consecutive spaces", "a good   example", "example good a"),
        ("Single word with spaces", "   word   ", "word"),
        ("Single word without spaces", "word", "word"),
        ("Empty string of spaces", "    ", ""),
        ("Mixed case with punctuation", "Bob  loves  Alice!", "Alice! loves Bob"),
    ]

    print("Running Tests for Problem 014: Reverse Words in a String\n" + "-" * 75)
    all_passed = True
    for name, s, expected in test_cases:
        res_py = reverse_words_pythonic(s)
        res_tp = reverse_words_two_pointers(s)
        
        passed = (res_py == expected) and (res_tp == expected)
        status = "PASSED" if passed else "FAILED"
        if not passed:
            all_passed = False
            
        print(f"[{status}] {name:30} | Input: '{s}' -> Output: '{res_tp}'")
        
    print("-" * 75)
    if all_passed:
        print("All test cases passed successfully! ")
