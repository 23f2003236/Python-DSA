# 🐍 Python DSA 100 — 25-Day Structured Mastery Roadmap

[![Language](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![DSA](https://img.shields.io/badge/DSA-100%20Problems-brightgreen.svg)]()
[![Target](https://img.shields.io/badge/Target-25%20Days-orange.svg)]()
[![Status](https://img.shields.io/badge/Progress-8%2F100-yellow.svg)]()

Welcome to the **Python DSA 100** repository! This is a 25-day interview preparation journey covering **100 carefully chosen Data Structures & Algorithms problems** frequently asked by top tech recruiters and FAANG/product companies.

Instead of randomly grinding hundreds of LeetCode questions, this roadmap focuses on **mastering ~25 core algorithmic patterns**. Once you understand the underlying pattern, you can solve any unseen variation in an interview.

---

## ⚡ Quick Links
- 📘 [Python DSA Cheat Sheet](cheatsheet.md) — Syntax, complexities, built-in methods, and 12 golden code templates.
- 🎯 [25-Day Daily Schedule](#-25-day-daily-schedule-4-problems--day)
- 🧠 [Algorithmic Patterns Map](#-algorithmic-patterns-map)
- 🏆 [5-Step Problem Solving Framework](#-the-5-step-problem-solving-framework)
- 🚀 [Git Workflow & How to Push](#-git-workflow--how-to-push)

---

## 📁 Repository Structure

Each phase has its own dedicated directory. Every problem file is self-contained with intuition, brute force, optimal solution, time/space complexity analysis, and runnable test cases:

```text
Python-DSA/
├── README.md                          # Master tracker and roadmap
├── cheatsheet.md                      # Quick revision guide & syntax cheat sheet
├── .gitignore                         # Python cache & temporary file ignore
├── 01_Foundations_Arrays_Strings/     # Problems 001 - 015
├── 02_Searching_and_Sorting/          # Problems 016 - 025
├── 03_Hashing_and_Prefix_Sum/         # Problems 026 - 035
├── 04_Two_Pointers_Sliding_Window/    # Problems 036 - 045
├── 05_Stack_and_Queue/                # Problems 046 - 055
├── 06_Linked_Lists/                   # Problems 056 - 065
├── 07_Recursion_and_Backtracking/     # Problems 066 - 075
├── 08_Trees_and_BST/                  # Problems 076 - 085
├── 09_Graphs/                         # Problems 086 - 095
└── 10_Dynamic_Programming/            # Problems 096 - 100
```

---

## 📅 25-Day Daily Schedule (4 Problems / Day)

### 🟢 Phase 1: Python & Foundations (Days 1–4)
Focus: Python syntax, time complexity basics, array traversals, two pointers, strings.

- [x] **Day 1: Array Foundations & Traversal (4/4 Completed)**
  - [x] [`001` — Find Maximum Element in Array](01_Foundations_Arrays_Strings/001_find_maximum_element.py) *(Array Traversal)*
  - [x] [`002` — Find Minimum Element in Array](01_Foundations_Arrays_Strings/002_find_minimum_element.py) *(Array Traversal)*
  - [x] [`003` — Find Second Largest Element](01_Foundations_Arrays_Strings/003_find_second_largest.py) *(Single Pass)*
  - [x] [`004` — Reverse an Array](01_Foundations_Arrays_Strings/004_reverse_an_array.py) *(Two Pointers)*
- [x] **Day 2: In-place Modifications & Basic Math (4/4 Completed)**
  - [x] [`005` — Check if Array is Sorted](01_Foundations_Arrays_Strings/005_check_if_array_is_sorted.py) *(Traversal)*
  - [x] [`006` — Remove Duplicates from Sorted Array](01_Foundations_Arrays_Strings/006_remove_duplicates_sorted_array.py) *(Two Pointers / In-place)*
  - [x] [`007` — Move Zeroes to End](01_Foundations_Arrays_Strings/007_move_zeroes_to_end.py) *(Two Pointers)*
  - [x] [`008` — Find Missing Number](01_Foundations_Arrays_Strings/008_find_missing_number.py) *(Math Formula / XOR)*
- [ ] **Day 3: Hashing & Frequency Counting**
  - [ ] `009` — Find Duplicate Number *(Hash Set / Floyd's Cycle)*
  - [ ] `010` — Frequency of Elements in Array *(Hash Map / Counter)*
  - [ ] `011` — First Non-Repeating Character in String *(Hash Map)*
  - [ ] `012` — Valid Anagram *(Frequency Count / Sorting)*
- [ ] **Day 4: String Manipulations & Boundary Handling**
  - [ ] `013` — Valid Palindrome String *(Two Pointers)*
  - [ ] `014` — Reverse Words in a String *(String Parsing / Two Pointers)*
  - [ ] `015` — Rotate Array by K Steps *(Array Reversal Algorithm)*
  - [ ] `016` — Linear Search *(Basic Searching)*

---

### 🟢 Phase 2: Searching & Sorting (Days 5–6)
Focus: Binary search patterns, Divide & Conquer, in-place sorting mechanisms.

- [ ] **Day 5: Binary Search Mastery**
  - [ ] `017` — Binary Search *(Iterative & Recursive)*
  - [ ] `018` — First Occurrence of an Element *(Modified Binary Search)*
  - [ ] `019` — Last Occurrence of an Element *(Modified Binary Search)*
  - [ ] `020` — Search Insert Position *(Binary Search Boundary)*
- [ ] **Day 6: Essential Sorting Algorithms**
  - [ ] `021` — Bubble Sort *(Swapping & Optimization Flag)*
  - [ ] `022` — Selection Sort *(Minimum Selection)*
  - [ ] `023` — Insertion Sort *(Shifting Elements)*
  - [ ] `024` — Merge Sort *(Divide and Conquer / Recursion)*

---

### 🟡 Phase 3: Hashing & Prefix Sum (Days 7–9)
Focus: $O(1)$ lookups, cumulative sums, frequency counts, sub-array tracking.

- [ ] **Day 7: Advanced Sorting & The Two Sum Family**
  - [ ] `025` — Quick Sort *(Partitioning & Pivot Selection)*
  - [ ] `026` — Two Sum *(Hash Map — Complement Lookup)*
  - [ ] `027` — Three Sum *(Sorting + Two Pointers)*
  - [ ] `028` — Intersection of Two Arrays *(Hash Set / Two Pointers)*
- [ ] **Day 8: Frequency, Voting & Set Invariants**
  - [ ] `029` — Union of Two Arrays *(Hash Set / Two Pointers)*
  - [ ] `030` — Majority Element (> n/2) *(Boyer-Moore Voting Algorithm)*
  - [ ] `031` — Longest Consecutive Sequence *(Hash Set — Streak Starter)*
  - [ ] `032` — Subarray With Given Sum *(Sliding Window / Prefix Sum)*
- [ ] **Day 9: Prefix Sum with Hash Map & Heaps**
  - [ ] `033` — Count Subarrays With Sum K *(Prefix Sum + Hash Map)*
  - [ ] `034` — Longest Subarray With Sum K *(Prefix Sum + First Seen Index)*
  - [ ] `035` — Top K Frequent Elements *(Hash Map + Min Heap / Bucket Sort)*
  - [ ] `036` — Sort Colors (0s, 1s, 2s) *(Dutch National Flag Algorithm)*

---

### 🟡 Phase 4: Two Pointers & Sliding Window (Days 10–11)
Focus: Shrinking/expanding windows, state tracking, subarray metrics.

- [ ] **Day 10: Two Pointers & Fixed Windows**
  - [ ] `037` — Container With Most Water *(Two Pointers — Greedy Invariant)*
  - [ ] `038` — Trapping Rain Water *(Two Pointers / Prefix Max)*
  - [ ] `039` — Maximum Subarray *(Kadane's Algorithm)*
  - [ ] `040` — Maximum Sum Subarray of Size K *(Fixed Sliding Window)*
- [ ] **Day 11: Dynamic / Variable Sliding Windows**
  - [ ] `041` — Longest Substring Without Repeating Characters *(Variable Window)*
  - [ ] `042` — Longest Repeating Character Replacement *(Sliding Window + Max Freq)*
  - [ ] `043` — Minimum Window Substring *(Sliding Window + Target Map)*
  - [ ] `044` — Permutation in String *(Fixed Window + Frequency Match)*

---

### 🟡 Phase 5: Stack & Queue (Days 12–14)
Focus: LIFO/FIFO, Monotonic Stack, Double-Ended Queues, caching structures.

- [ ] **Day 12: Stack & Queue Fundamentals**
  - [ ] `045` — Minimum Size Subarray Sum *(Sliding Window)*
  - [ ] `046` — Implement Stack Using List *(LIFO Mechanics)*
  - [ ] `047` — Implement Queue Using Deque *(FIFO Mechanics)*
  - [ ] `048` — Min Stack in O(1) Time *(Auxiliary Stack / Value Pairing)*
- [ ] **Day 13: Classic Stack & Monotonic Stack**
  - [ ] `049` — Valid Parentheses *(Stack Matching)*
  - [ ] `050` — Evaluate Reverse Polish Notation *(Stack Evaluation)*
  - [ ] `051` — Next Greater Element *(Monotonic Decreasing Stack)*
  - [ ] `052` — Daily Temperatures *(Monotonic Stack Index Tracking)*
- [ ] **Day 14: Advanced Stack & Queue**
  - [ ] `053` — Largest Rectangle in Histogram *(Monotonic Stack)*
  - [ ] `054` — Sliding Window Maximum *(Monotonic Deque)*
  - [ ] `055` — LRU Cache *(Hash Map + Doubly Linked List)*
  - [ ] `056` — Implement Singly Linked List *(Node class, Insert, Delete, Traverse)*

---

### 🟠 Phase 6: Linked Lists (Days 15–16)
Focus: Pointer rewiring, dummy heads, slow & fast pointer techniques.

- [ ] **Day 15: Traversal, Reversal & Cycles**
  - [ ] `057` — Reverse a Linked List *(Iterative & Recursive)*
  - [ ] `058` — Find Middle of Linked List *(Slow & Fast Pointer)*
  - [ ] `059` — Detect Cycle in Linked List *(Floyd's Tortoise & Hare)*
  - [ ] `060` — Find Cycle Starting Node *(Floyd's Cycle Entry Proof)*
- [ ] **Day 16: Multi-List Manipulation & Reordering**
  - [ ] `061` — Merge Two Sorted Lists *(Dummy Node + Two Pointers)*
  - [ ] `062` — Remove Nth Node From End of List *(Two Pointers Gap)*
  - [ ] `063` — Add Two Numbers as Linked Lists *(Carry Propagation)*
  - [ ] `064` — Reorder List *(Middle + Reverse + Alternating Merge)*

---

### 🟠 Phase 7: Recursion & Backtracking (Days 17–19)
Focus: Decision trees, state rollback (choose-explore-unchoose), pruning.

- [ ] **Day 17: Recursion Basics to Subsets**
  - [ ] `065` — Merge K Sorted Lists *(Min Heap / Divide & Conquer)*
  - [ ] `066` — Factorial of a Number *(Recursion & Stack Trace)*
  - [ ] `067` — N-th Fibonacci Number *(Recursion vs Memoization)*
  - [ ] `068` — Generate All Subsets / Power Set *(Backtracking / Cascading)*
- [ ] **Day 18: Combinations & Permutations**
  - [ ] `069` — Generate Permutations *(Backtracking with Swaps / Visited Set)*
  - [ ] `070` — Combination Sum *(Backtracking with Reusable Elements)*
  - [ ] `071` — Generate Parentheses *(Backtracking with Open/Close Constraints)*
  - [ ] `072` — Letter Combinations of a Phone Number *(Combinatorial Backtracking)*
- [ ] **Day 19: Grid Backtracking & Pruning**
  - [ ] `073` — N-Queens Problem *(Board Validation Backtracking)*
  - [ ] `074` — Word Search in 2D Grid *(DFS + Backtracking with Visited Grid)*
  - [ ] `075` — Sudoku Solver *(Constraint Satisfaction Backtracking)*
  - [ ] `076` — Binary Tree Preorder Traversal *(DFS Recursive & Iterative)*

---

### 🔴 Phase 8: Trees & Binary Search Trees (Days 20–22)
Focus: Tree recursion, DFS vs BFS, BST invariants, serialization.

- [ ] **Day 20: Tree Traversals & Depth**
  - [ ] `077` — Binary Tree Inorder Traversal *(Left-Root-Right)*
  - [ ] `078` — Binary Tree Postorder Traversal *(Left-Right-Root)*
  - [ ] `079` — Binary Tree Level Order Traversal *(BFS with Queue)*
  - [ ] `080` — Maximum Depth / Height of Binary Tree *(DFS Bottom-up)*
- [ ] **Day 21: Tree Properties & BST Operations**
  - [ ] `081` — Diameter of Binary Tree *(Bottom-up Height + Global Max)*
  - [ ] `082` — Validate Binary Search Tree *(Range `(low, high)` Validation)*
  - [ ] `083` — Lowest Common Ancestor (LCA) in BST & Binary Tree *(DFS)*
  - [ ] `084` — Kth Smallest Element in BST *(Inorder Traversal Property)*
- [ ] **Day 22: Advanced Tree & Graph Intro**
  - [ ] `085` — Serialize and Deserialize Binary Tree *(Preorder / Level Order)*
  - [ ] `086` — Implement Graph Using Adjacency List *(Directed & Undirected)*
  - [ ] `087` — Breadth First Search (BFS) on Graph *(Queue + Visited Set)*
  - [ ] `088` — Depth First Search (DFS) on Graph *(Recursive & Stack)*

---

### 🔴 Phase 9: Graphs (Days 23–24)
Focus: BFS/DFS traversals, cycles, topological sorting, shortest paths.

- [ ] **Day 23: Connected Components & Cycles**
  - [ ] `089` — Number of Islands *(2D Grid BFS / DFS)*
  - [ ] `090` — Clone Graph *(DFS/BFS with Hash Map Clone Memo)*
  - [ ] `091` — Detect Cycle in Undirected Graph *(DFS / BFS with Parent)*
  - [ ] `092` — Detect Cycle in Directed Graph *(DFS with Recursion Stack / Color)*
- [ ] **Day 24: Topological Sort & Shortest Paths**
  - [ ] `093` — Course Schedule *(Topological Sort / Kahn's Algorithm / In-degree)*
  - [ ] `094` — Number of Connected Components *(DFS / Union-Find)*
  - [ ] `095` — Dijkstra's Shortest Path Algorithm *(Min Heap + Adjacency)*
  - [ ] `096` — Climbing Stairs *(1D Dynamic Programming — Fibonacci Pattern)*

---

### 🔥 Phase 10: Dynamic Programming (Day 25)
Focus: Overlapping subproblems, optimal substructure, transitions, knapsack patterns.

- [ ] **Day 25: Classic DP Patterns & Final Mastery**
  - [ ] `097` — House Robber *(1D DP — Include / Exclude Choice)*
  - [ ] `098` — Coin Change *(Unbounded Knapsack / Minimum Steps DP)*
  - [ ] `099` — Longest Common Subsequence (LCS) *(2D DP Grid Matching)*
  - [ ] `100` — 0/1 Knapsack Problem *(Classic 2D / 1D Optimized DP)*

---

## 🧠 Algorithmic Patterns Map

| Pattern | Problems Covered |
| :--- | :--- |
| **Two Pointers** | `004`, `006`, `007`, `013`, `014`, `027`, `036`, `037`, `038` |
| **Sliding Window** | `032`, `040`, `041`, `042`, `043`, `044`, `045`, `054` |
| **Hash Map / Frequency** | `009`, `010`, `011`, `012`, `026`, `028`, `029`, `031`, `035` |
| **Prefix Sum** | `032`, `033`, `034` |
| **Binary Search** | `017`, `018`, `019`, `020` |
| **Monotonic Stack** | `051`, `052`, `053` |
| **Fast & Slow Pointers** | `058`, `059`, `060`, `064` |
| **Backtracking** | `068`, `069`, `070`, `071`, `072`, `073`, `074`, `075` |
| **Tree DFS / BFS** | `076`, `077`, `078`, `079`, `080`, `081`, `082`, `083`, `084`, `085` |
| **Graph Traversals & Topo Sort** | `087`, `088`, `089`, `090`, `091`, `092`, `093`, `094`, `095` |
| **Dynamic Programming** | `096`, `097`, `098`, `099`, `100` |

---

## 🏆 The 5-Step Problem Solving Framework

In technical interviews, writing the code is only step 4. Recruiters evaluate how you think:

```text
1. Understand & Clarify
   ├── Rephrase problem in your own words
   └── Ask about constraints: negative numbers? empty input? scale of N?

2. Brute Force & Bottleneck
   ├── State the obvious brute-force solution (e.g., O(n²))
   └── Ask: "What am I recomputing?" -> "Can a Hash Map, Two Pointers, or Sorting eliminate this?"

3. State the Invariant / Algorithm
   ├── Explain the intuition before touching the keyboard
   └── "We maintain a window [left, right] where all characters are unique..."

4. Write Clean Python
   ├── Idiomatic naming, type hints, minimal boilerplate
   └── Leverage collections, heapq, bisect where appropriate

5. Verify Complexity & Edge Cases
   ├── State Time: O(...) and Space: O(...)
   └── Walk through test cases: empty list, 1 element, duplicates, negatives
```

---

## 🚀 Git Workflow & How to Push

The repository is already initialized and linked to your GitHub repository:
`https://github.com/23f2003236/Python-DSA.git`

### Whenever you want to push commits to GitHub:
Open PowerShell / Terminal in this folder and run:

```bash
git push -u origin main
```

*(Git Credential Manager will authenticate your account once, and subsequent pushes will happen automatically with just `git push`).*

---

**Happy Problem Solving! 🚀 Stay consistent, understand the patterns, and celebrate every completed milestone.**
