

# Three Sum Comparison

**Author:** Tahmeed Bin Mahabub  

This project demonstrates multiple approaches to solving the **Three Sum** problem — finding triplets in a list that add up to a target value.  
Each version improves upon the previous one in terms of logic, performance, or optimization. It’s great for understanding time complexity, iteration cost, and hash map usage in Python.

---

## Description

The program implements **four versions** of the Three Sum algorithm:

| Version | Approach | Highlights |
|----------|-----------|-------------|
| **V1** | Basic Brute Force | Checks all combinations, no duplicate index check |
| **V2** | Improved Brute Force | Skips reuse of the same index |
| **V3** | Hash Map for Pair Sums | Stores pair sums in a hash map for faster lookup |
| **V4** | Optimized Hash Map | Builds and checks sums dynamically to reduce redundant operations |

Each approach counts how many iterations it takes and prints both the results and performance details.

---

## How to Run

### 1. Clone or download the project
```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Run the Script
```bash
python sum_of_three.py
```

####  Eaxample Output
``` 
==============================
🔹 Version 1: Basic Brute Force
==============================
Results: [[1, 2, 3]]
Total Iterations: 125 

==============================
🔹 Version 2: Improved Brute Force
==============================
Results: [[1, 2, 3]]
Total Iterations: 60 

==============================
🔹 Version 3: Hash Map for Pair Sums
==============================
Results: [[1, 2, 3]]
Total Iterations: 31 

==============================
🔹 Version 4: Optimized Hash Map
==============================
Results: [[1, 2, 3]]
Total Iterations: 20 

✅ Comparison Complete
```
### 3. How to Stop
```bash
CRTL + c

```
