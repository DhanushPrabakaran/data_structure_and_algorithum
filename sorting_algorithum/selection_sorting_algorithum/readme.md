# Selection Sort Algorithm

Selection Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

---

## 📌 Features

- Easy-to-understand implementation
- Works on arrays or lists
- Best for learning sorting concepts
- Time complexity analysis included

---

## 🧠 How Selection Sort Works

1. Compare the first two elements.
2. If the first is greater than the second, swap them.
3. Move to the next pair and repeat step 2.
4. Continue until the end of the array.
5. Repeat the entire process for `n-1` passes (where `n` is the array length) or until no swaps are needed.

---

## 📈 Time and Space Complexity

| Case        | Time Complexity | Explanation             |
|-------------|-----------------|-------------------------|
| Best Case   | O(n)            | When the list is sorted |
| Average Case| O(n²)           | Random order            |
| Worst Case  | O(n²)           | Reverse sorted          |

- **Space Complexity**: O(1) – No extra memory is used
- **Stable Sort**: ✅
- **In-Place Sort**: ✅

---

## ✅ Advantages

- Simple to implement
- Easy to understand for beginners
- Doesn't require additional memory

---

## ❌ Disadvantages

- Very slow on large lists
- Not suitable for performance-critical applications

---
