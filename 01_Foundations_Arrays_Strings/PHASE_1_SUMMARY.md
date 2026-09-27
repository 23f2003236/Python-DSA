# 🧠 Phase 1: Python & Foundations — Must-Know Summary & Cheat Sheet

> **Welcome to the Phase 1 Mastery Summary!**  
> In Problems `001` through `016`, you mastered the foundational building blocks of Data Structures & Algorithms. Every technical interview at top product companies tests these core patterns.

---

## 📌 The 5 Core Mental Models of Phase 1

### 1. Single-Pass Invariant Maintenance (Problems 001, 002, 003, 005)
- **Concept:** As you iterate through an array once, maintain a "running state" or "invariant" of what you have seen so far (`current_max`, `current_min`, `first` and `second` largest).
- **Gold & Silver Medal Pattern (Problem 003):**
  - If a new number beats `first`, demote `first` to `second`, and update `first = num`.
  - If it beats `second` (and is distinct from `first`), update `second = num`.
- **Early Exit (Problem 005 & 016):**
  - Stop the loop the instant an invariant is violated (e.g., `nums[i] > nums[i+1]` means not sorted). Never keep looping if the answer is already determined!

---

### 2. Two Pointers: Opposite Ends Technique (Problems 004, 013)
- **Concept:** One pointer starts at the left boundary (`0`) and the other at the right boundary (`len - 1`), moving inward toward each other (`left < right`).
- **Use Cases:**
  - In-place Array Reversal (`nums[left], nums[right] = nums[right], nums[left]`).
  - Palindrome verification with skipping non-alphanumeric characters.
- **Space Benefit:** Strictly $\mathcal{O}(1)$ space! No extra arrays allocated.

---

### 3. Two Pointers: Slow & Fast / Reader & Writer (Problems 006, 007)
- **Concept:** Both pointers move in the same direction, but at different speeds or conditions.
  - `write_ptr` (Slow): Marks where the next valid/unique element should be written.
  - `read_ptr` (Fast): Scans ahead exploring new elements.
- **In-place Array Compaction:**
  - Removing duplicates: `if nums[read] != nums[write]: write += 1; nums[write] = nums[read]`
  - Moving zeroes: `if nums[curr] != 0: nums[pos], nums[curr] = nums[curr], nums[pos]; pos += 1`

---

### 4. Hashing & Frequency Counting (Problems 009, 010, 011, 012)
- **Concept:** Trade $\mathcal{O}(n)$ auxiliary memory for instant $\mathcal{O}(1)$ average lookups.
- **The 3 Essential Tools:**
  1. `dict`: Universal across all languages (`dict.get(k, 0) + 1`).
  2. `collections.defaultdict(int)`: Automatic zero initialization.
  3. `collections.Counter(iterable)`: Instant frequency map.
- **Floyd's Tortoise and Hare (Problem 009):**
  - Turning an array into a functional graph/linked list (`i -> nums[i]`).
  - Detecting cycles in $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ space using slow/fast pointers.

---

### 5. Modulo Arithmetic & The 3-Step Reversal (Problems 008, 014, 015)
- **Modulo Normalization:** `k = k % n`. When shifting or rotating cyclically, a full circle brings you back to the start.
- **3-Step In-Place Rotation Algorithm (Problem 015):**
  1. Reverse entire array: `reverse(0, n - 1)`
  2. Reverse first $k$ elements: `reverse(0, k - 1)`
  3. Reverse remaining $n - k$ elements: `reverse(k, n - 1)`
- **Bitwise XOR Cancellation (Problem 008):**
  - $a \oplus a = 0$ and $a \oplus 0 = a$.
  - Avoids integer overflow in 32-bit systems when finding missing numbers.

---

## ⚡ Phase 1 Time & Space Complexity Master Sheet

| Problem | Method / Pattern | Time Complexity | Auxiliary Space | In-Place? |
| :--- | :--- | :--- | :--- | :--- |
| **001: Find Maximum** | Linear Scan | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **002: Find Minimum** | Linear Scan | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **003: Second Largest** | Single Pass Multi-state | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **004: Reverse Array** | Two Pointers (Opposite Ends) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **005: Check if Sorted** | Linear Traversal + Early Exit | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **006: Remove Duplicates** | Slow & Fast Pointers | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **007: Move Zeroes** | Two Pointers Swap | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **008: Missing Number** | Gauss Sum / Bitwise XOR | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **009: Find Duplicate** | Floyd's Cycle Detection | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **010: Frequency Counting**| Hash Map / Counter | $\mathcal{O}(n)$ | $\mathcal{O}(k)$ | No |
| **011: First Unique Char** | Two-Pass Hash Map Scan | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ (fixed 26) | No |
| **012: Valid Anagram** | Frequency Balancing | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ (fixed 26) | No |
| **013: Valid Palindrome** | Two Pointers Inward Scan | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **014: Reverse Words** | Two Pointers / Tokenization | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | No (Strings immutable) |
| **015: Rotate Array by K** | 3-Step Array Reversal | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |
| **016: Linear Search** | Sequential Scan + Early Exit | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes |

---

## ⚠️ The Top 5 Recruiter Traps to Avoid

1. **Initializing with 0 instead of `nums[0]` or `float('-inf')`:**
   - Always assume negative numbers exist in the input unless specified otherwise!
2. **Calling `s.count()` or `nums.count()` inside a loop:**
   - `.count()` is an $\mathcal{O}(n)$ operation. Calling it inside a loop makes your code $\mathcal{O}(n^2)$!
3. **Using `nums.pop(0)` or `del nums[0]`:**
   - Deleting from index 0 forces Python to shift all $n - 1$ elements to the left ($\mathcal{O}(n)$). Use `collections.deque.popleft()` instead.
4. **Confusing Slicing with In-Place Mutation:**
   - `nums[::-1]` creates a brand new copy of the list. When asked for in-place with $\mathcal{O}(1)$ memory, use two pointers!
5. **Forgetting `k = k % n` in Array Rotation:**
   - If $k \ge n$, direct slicing or shifting without modulo results in an `IndexError` or unnecessary redundant rotations.
