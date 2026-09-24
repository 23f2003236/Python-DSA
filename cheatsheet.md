# ⚡ Python DSA Quick Revision Cheat Sheet

> **Keep this file open during your DSA practice.** Whenever you forget a syntax, method, time complexity, or algorithmic pattern template, this is your single source of truth.

---

## 📌 Table of Contents
1. [Big-O Time & Space Complexity Reference](#1-big-o-complexity-reference)
2. [Python Built-in Data Structures & Methods](#2-python-built-in-data-structures--methods)
   - [Lists (Dynamic Arrays)](#a-lists-dynamic-arrays)
   - [Strings](#b-strings)
   - [Dictionaries (Hash Maps)](#c-dictionaries-hash-maps)
   - [Sets (Hash Sets)](#d-sets-hash-sets)
   - [Deques (Double-Ended Queues / Stacks)](#e-deque-collectionsdeque)
   - [Heaps / Priority Queues (`heapq`)](#f-heaps--priority-queues-heapq)
   - [Binary Search (`bisect`)](#g-binary-search-bisect)
3. [Useful Python Math & Bitwise Utilities](#3-useful-python-math--bitwise-utilities)
4. [The 12 Essential Algorithmic Templates](#4-the-12-essential-algorithmic-templates)
5. [Interview Edge Cases Checklist](#5-interview-edge-cases-checklist)

---

## 1. Big-O Complexity Reference

### ⏱️ Time Complexity of Common Operations

| Data Structure / Operation | Access | Search | Insert | Delete | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Python List (Array)** | $O(1)$ | $O(n)$ | $O(1)$ at end, $O(n)$ at middle/front | $O(1)$ at end, $O(n)$ at middle/front | $O(n)$ |
| **Hash Map (`dict`)** | N/A | $O(1)$ avg | $O(1)$ avg | $O(1)$ avg | $O(n)$ |
| **Hash Set (`set`)** | N/A | $O(1)$ avg | $O(1)$ avg | $O(1)$ avg | $O(n)$ |
| **Deque (`collections.deque`)** | $O(n)$ middle | $O(n)$ | $O(1)$ both ends | $O(1)$ both ends | $O(n)$ |
| **Min Heap (`heapq`)** | $O(1)$ peek min | $O(n)$ | $O(\log n)$ | $O(\log n)$ pop min | $O(n)$ |
| **Singly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ if pointer known | $O(1)$ if pointer known | $O(n)$ |
| **Binary Search Tree (Balanced)** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |

### ⚡ Sorting Algorithms Summary

| Algorithm | Best Time | Average Time | Worst Time | Space | Stable? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No |
| **Python `sorted()` / `.sort()` (Timsort)** | $O(n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |

---

## 2. Python Built-in Data Structures & Methods

### A. Lists (Dynamic Arrays)

```python
nums = [10, 20, 30, 40]

# Add elements
nums.append(50)          # O(1) amortized - adds to end
nums.insert(0, 5)        # O(n) - shifts all elements right! AVOID in loops

# Remove elements
val = nums.pop()         # O(1) - removes and returns last element
val = nums.pop(0)        # O(n) - shifts everything left! Use deque instead
nums.remove(20)          # O(n) - finds first occurrence and removes

# Slicing tricks (All slicing creates a SHALLOW COPY: O(k) time & space)
rev = nums[::-1]         # Reverse a list
sub = nums[1:4]          # Subarray from index 1 to 3
copy = nums[:]           # Shallow copy

# In-place reverse and sort
nums.reverse()           # O(n) in-place reverse
nums.sort()              # O(n log n) in-place ascending
nums.sort(reverse=True)  # O(n log n) descending
nums.sort(key=lambda x: (x[0], -x[1])) # Custom sort by multiple criteria

# Useful functions
length = len(nums)       # O(1)
total = sum(nums)        # O(n)
minimum = min(nums)      # O(n)
maximum = max(nums)      # O(n)
```

> ⚠️ **Common Trap**: Never use `nums.pop(0)` or `nums.insert(0, val)` inside a loop of size $n$, because that turns an $O(n)$ algorithm into an $O(n^2)$ bottleneck. Use `collections.deque` instead.

---

### B. Strings

Strings in Python are **immutable**. Any modification creates a new string.

```python
s = "leetcode"

# String traversal
for ch in s:
    pass

# Checking character properties
s.isalpha()              # True if letters only
s.isdigit()              # True if digits only
s.isalnum()              # True if letters or digits
s.islower() / s.isupper()

# ASCII values
ascii_code = ord('a')    # 97
char = chr(97)           # 'a'

# Fast string building (Always use join instead of '+' in loops!)
chars = ['a', 'b', 'c']
result = "".join(chars)  # O(n) time, very efficient

# Splitting and trimming
words = "hello world".split()      # Splits by whitespace
trimmed = "  spaced  ".strip()     # Removes leading/trailing spaces
```

---

### C. Dictionaries (Hash Maps)

```python
# Standard Dict
counts = {}
counts["apple"] = counts.get("apple", 0) + 1  # Safe access with default

# Iterating
for key, value in counts.items():
    print(key, value)

# collections.defaultdict (avoids KeyError automatically)
from collections import defaultdict

freq = defaultdict(int)         # default value is 0
graph = defaultdict(list)       # default value is []
groups = defaultdict(set)       # default value is set()

freq["apple"] += 1              # No need to check if "apple" exists!
graph[1].append(2)              # Automatically appends 2 to empty list

# collections.Counter (instant frequency map)
from collections import Counter
c = Counter([1, 2, 2, 3, 3, 3]) # {3: 3, 2: 2, 1: 1}
top_2 = c.most_common(2)        # [(3, 3), (2, 2)]
```

---

### D. Sets (Hash Sets)

```python
seen = set()

# Adding and removing
seen.add(10)             # O(1) avg
seen.discard(10)         # O(1) avg - does not raise error if not found
seen.remove(10)          # O(1) avg - raises KeyError if not found

# Membership test
if 10 in seen:           # O(1) average lookup (vs O(n) for list)
    pass

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}
union = a | b            # {1, 2, 3, 4}
intersection = a & b     # {2, 3}
difference = a - b       # {1}
```

---

### E. Deque (`collections.deque`)

Double-ended queue. Ideal for **Queues (FIFO)**, **Stacks (LIFO)**, and **BFS**.

```python
from collections import deque

dq = deque()

# Right side operations (O(1))
dq.append(10)
val = dq.pop()

# Left side operations (O(1) - huge advantage over list!)
dq.appendleft(5)
val = dq.popleft()

# Peek elements
first = dq[0]
last = dq[-1]
```

---

### F. Heaps / Priority Queues (`heapq`)

Python's `heapq` implements a **Min Heap** by default.

```python
import heapq

min_heap = []

# Push & Pop (O(log n))
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 15)

smallest = heapq.heappop(min_heap)      # Returns 4 (peek with min_heap[0])

# Transform an existing list into a heap in O(n) time
nums = [5, 1, 9, 3]
heapq.heapify(nums)                     # nums is now a valid min heap

# Max Heap trick: Multiply numbers by -1
max_heap = []
heapq.heappush(max_heap, -val)
largest = -heapq.heappop(max_heap)

# Heap with tuples (sorts by 1st element; tie-breaker is 2nd element)
heapq.heappush(min_heap, (priority, item))
```

---

### G. Binary Search (`bisect`)

```python
import bisect

arr = [10, 20, 20, 30, 40]

# bisect_left: leftmost insertion index (first element >= target)
idx_left = bisect.bisect_left(arr, 20)    # Returns index 1

# bisect_right: rightmost insertion index (first element > target)
idx_right = bisect.bisect_right(arr, 20)  # Returns index 3

# Insert into sorted list while maintaining sorted order
bisect.insort(arr, 25)
```

---

## 3. Useful Python Math & Bitwise Utilities

```python
# Infinity values (great for min/max initialization)
INF = float('inf')
NEG_INF = float('-inf')

# Integer division and modulo
quotient = 7 // 2       # 3
remainder = 7 % 2       # 1
q, r = divmod(7, 2)     # (3, 1) in one shot

# Bitwise Operations
a & b   # Bitwise AND
a | b   # Bitwise OR
a ^ b   # Bitwise XOR (Properties: x ^ x = 0, x ^ 0 = x)
~a      # Bitwise NOT
a << 1  # Left shift (multiply by 2)
a >> 1  # Right shift (integer divide by 2)

# Check if n is power of 2
is_power_of_two = (n > 0) and (n & (n - 1) == 0)

# Check if k-th bit is set (0-indexed from right)
is_set = (n >> k) & 1
```

---

## 4. The 12 Essential Algorithmic Templates

### 1. Two Pointers (Opposite Ends)
Used for: Sorted Array Two Sum, Palindrome validation, Container With Most Water.
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### 2. Fast & Slow Pointers (Floyd's Cycle Finding)
Used for: Linked List cycle detection, middle node, happy numbers.
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### 3. Sliding Window (Fixed Size $K$)
Used for: Maximum sum subarray of size $K$.
```python
def max_sub_array_k(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

### 4. Sliding Window (Dynamic / Variable Size)
Used for: Longest substring without repeating characters, Minimum window substring.
```python
def dynamic_sliding_window(s):
    left = 0
    state = {}
    best_len = 0
    for right in range(len(s)):
        # 1. Expand: include s[right]
        state[s[right]] = state.get(s[right], 0) + 1
        
        # 2. Shrink: while condition is violated
        while condition_violated:
            state[s[left]] -= 1
            left += 1
            
        # 3. Update best result
        best_len = max(best_len, right - left + 1)
    return best_len
```

### 5. Prefix Sum + Hash Map
Used for: Subarray sum equals $K$, Longest subarray with sum $K$.
```python
def subarray_sum(nums, k):
    prefix_map = {0: 1}  # {prefix_sum: frequency}
    current_sum = 0
    count = 0
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_map:
            count += prefix_map[current_sum - k]
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
    return count
```

### 6. Binary Search (Standard Template)
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2  # prevents overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### 7. Monotonic Stack (Next Greater Element)
```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
```

### 8. Reverse a Linked List (Iterative)
```python
def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

### 9. Tree Traversals (DFS & BFS)
```python
# DFS - Recursive (Inorder)
def inorder(root, res):
    if not root:
        return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)

# BFS - Level Order (Queue)
from collections import deque
def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

### 10. Graph Traversal (BFS & DFS with Adjacency List)
```python
from collections import deque

# BFS on Graph
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS on Graph (Iterative)
def dfs(graph, start):
    visited = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
```

### 11. Backtracking Template
Used for: Subsets, Permutations, Combination Sum, N-Queens.
```python
def backtrack(start_index, current_path, results):
    if is_solution(current_path):
        results.append(list(current_path))
        return
    
    for i in range(start_index, len(candidates)):
        # 1. Choose
        current_path.append(candidates[i])
        # 2. Explore
        backtrack(i + 1, current_path, results)
        # 3. Unchoose (backtrack)
        current_path.pop()
```

### 12. Dynamic Programming (1D / 2D)
```python
# Top-Down with Memoization
memo = {}
def dp(i):
    if base_condition:
        return base_value
    if i in memo:
        return memo[i]
    memo[i] = solve(dp(i - 1), dp(i - 2))
    return memo[i]

# Bottom-Up Tabulation
def dp_bottom_up(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

---

## 5. Interview Edge Cases Checklist

Before presenting your final answer to an interviewer, run through this mental checklist:

1. **Empty / Null Input**: `nums = []`, `head = None`, `s = ""`
2. **Single Element**: `nums = [42]`, `s = "a"`
3. **Two Elements**: `nums = [1, 2]`, `nums = [2, 1]`
4. **All Duplicates**: `nums = [7, 7, 7, 7]`
5. **Already Sorted / Reverse Sorted**: `nums = [1, 2, 3, 4]`, `nums = [4, 3, 2, 1]`
6. **Negative Numbers & Zero**: `[-5, 0, 5]` (critical for sum/product problems)
7. **Extreme Constraints**:
   - $n = 10^5 \implies$ Solution MUST be $O(n)$ or $O(n \log n)$ ($O(n^2)$ will TLE).
   - $n \le 20 \implies$ Exponential $O(2^n)$ backtracking is expected.
   - $n \le 500 \implies O(n^2)$ or $O(n^3)$ DP is acceptable.
8. **Linked List Cycles**: Missing next pointer updates causing infinite loops.
9. **Off-by-One Errors**: Check loop boundaries (`range(n)` vs `range(n - 1)`).
