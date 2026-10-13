"""
╔══════════════════════════════════════════════════════════════════════╗
║         FIBONACCI SERIES GENERATOR - BTech CSE (2nd Year)           ║
║                    Data Structures & Algorithms                      ║
╚══════════════════════════════════════════════════════════════════════╝

CONCEPTS COVERED:
  - Iteration (Loops)
  - Recursion

"""




# ─────────────────────────────────────────────────────────────────────────────
# METHOD 1: Iterative Approach — O(n) Time, O(1) Space
# ─────────────────────────────────────────────────────────────────────────────
def fibonacci_iterative(n):
    """
    Generate Fibonacci series up to n terms using iteration.
    Time Complexity  : O(n)
    Space Complexity : O(n)  [to store the list]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    series = [0, 1]
    for i in range(2, n):
        series.append(series[i-1] + series[i-2])
    return series


# ─────────────────────────────────────────────────────────────────────────────
# METHOD 2: Recursive Approach — O(2^n) Time, O(n) Space
# ─────────────────────────────────────────────────────────────────────────────
def fibonacci_recursive(n):
    """
    Return the nth Fibonacci number using pure recursion.
    Time Complexity  : O(2^n)  ← Exponential (slow for large n)
    Space Complexity : O(n)    [call stack depth]
    
    NOTE: Not recommended for n > 30 due to performance.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_recursive_series(n):
    """Generate series using the recursive function."""
    return [fibonacci_recursive(i) for i in range(n)]


# ─────────────────────────────────────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────────────────────────────────────
def print_banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║        FIBONACCI SERIES GENERATOR — BTech CSE 2nd Year       ║
╠══════════════════════════════════════════════════════════════╣
║  Methods Available:                                          ║
║    1. Iterative          — O(n) time, O(1) space             ║
║    2. Recursive          — O(2^n) time (demo only)           ║
╚══════════════════════════════════════════════════════════════╝
""")

def main():
    print_banner()

    while True:
        print("  MAIN MENU")
        print("  ─────────────────────────────────────")
        print("  [1]  Generate series (choose method)")
        print("  [0]  Exit")
        print()

        choice = input("  Enter your choice: ").strip()

        if choice == "0":
            print("\n  Goodbye! Keep coding. 🚀\n")
            break

        elif choice == "1":
            try:
                n = int(input("  Enter number of terms: "))
                if n <= 0:
                    print("  Please enter a positive integer.\n")
                    continue
                print("\n  Select Method:")
                print("  [1] Iterative  [2] Recursive (n≤30)")
                m = input("  Method: ").strip()
                print()
                if m == "1":
                    print(f"  Result: {fibonacci_iterative(n)}")
                elif m == "2":
                    if n > 30:
                        print("  ⚠  Recursive is too slow for n > 30. Limiting to 30.")
                        n = 30
                    print(f"  Result: {fibonacci_recursive_series(n)}")
                else:
                    print("  Invalid method choice.")
            except ValueError:
                print("  Please enter a valid integer.\n")

        else:
            print("  Invalid choice. Please try again.\n")

        print()  # spacing


# ─────────────────────────────────────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
