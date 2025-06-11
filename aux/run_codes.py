import sys
import re

def freeze():
    breakpoint()


if __name__ == '__main__':

    pattern_docs = [
        "✅ Pattern 01 : Sliding Window",
        "✅ Pattern 02: Two Pointers",
        "✅ Pattern 03: Fast & Slow pointers",
        "✅ Pattern 04 : Merge Intervals",
        "✅ Pattern 05: Cyclic Sort",
        "✅ Pattern 06: In-place Reversal of a LinkedList",
        "✅ Pattern 07: Tree Breadth First Search",
        "✅ Pattern 08:Tree Depth First Search",
        "✅ Pattern 09: Two Heaps",
        "✅ Pattern 09: Two Heaps",
        "✅ Pattern 10: Subsets",
        "✅ Pattern 11: Modified Binary Search",
        "✅ Pattern 12:  Bitwise XOR",
        "✅ Pattern 13: Top 'K' Elements",
        "✅ Pattern 14: K-way merge",
        "✅ Pattern 15: 0-1 Knapsack (Dynamic Programming)",
        "✅ Pattern 16: 🔎 Topological Sort (Graph)"
    ]

    chosen_pattern = int(sys.argv[-1]) - 1
    with open(pattern_docs[chosen_pattern] + '.md', 'r') as f:
        text = f.read()
        python_codes = re.findall('```python\n.*?\n\n\n', text, flags=re.DOTALL)
        for code in python_codes:
            # Ignoring "```python" text and importing
            exec(code[9:])
        freeze()
