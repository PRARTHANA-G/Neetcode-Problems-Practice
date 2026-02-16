from typing import List

# Approach: Use a set to track seen numbers
# Why set: O(1) lookup vs O(n) lookup for list
# Time: O(n) - single pass through array
# Space: O(n) - set grows up to size of input
# Key insight: sets use hashing = instant lookup

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False


def run_with_steps(nums: List[int]) -> bool:
    
    seen = set()
    print(f"\n{'='*40}")
    print(f"Input array: {nums}")
    print(f"{'='*40}")

    for i in range(len(nums)):
        print(f"\nStep {i+1}: Checking nums[{i}] = {nums[i]}")
        print(f"  Current 'seen' set: {seen}")

        if nums[i] in seen:
            print(f"   {nums[i]} is ALREADY in seen!")
            print(f"  → Duplicate found! Returning True")
            return True
        else:
            seen.add(nums[i])
            print(f"   {nums[i]} not in seen yet, adding it.")
            print(f"  Updated 'seen' set: {seen}")

    print(f"\n  → No duplicates found! Returning False")
    return False


def get_input():
    """Get array input from user."""
    print("\n" + "="*40)
    print("   CONTAINS DUPLICATE - INTERACTIVE")
    print("="*40)
    print("Enter numbers separated by spaces.")
    print("Example: 1 2 3 4  or  1 2 3 1")
    print("-"*40)

    while True:
        try:
            raw = input("Enter your array: ").strip()
            nums = list(map(int, raw.split()))
            if len(nums) == 0:
                print("Please enter at least one number.")
                continue
            return nums
        except ValueError:
            print("Invalid input. Please enter integers only (e.g. 1 2 3 4)")


def main():
    while True:
        # Get input from user
        nums = get_input()

        # Run with step by step visualization
        result = run_with_steps(nums)

        # Final answer
        print(f"\n{'='*40}")
        print(f"FINAL ANSWER: {result}")
        if result:
            print("This array HAS duplicates.")
        else:
            print("This array has NO duplicates.")
        print(f"{'='*40}")

        # Ask if they want to try again
        again = input("\nTry another array? (y/n): ").strip().lower()
        if again != 'y':
            print("\nGood work! Commit this to GitHub.")
            break


if __name__ == "__main__":
    main()



#seen = []
# Python checks every single element one by one
# [1, 2, 3, 4, 5....] → checks 1, then 2, then 3...
# Time: O(n) for EACH lookup
# Total: O(n²) → slow

#seen = set()
# Python uses hashing - goes DIRECTLY to the answer
# Like a dictionary with keys only
# Time: O(1) for EACH lookup
# Total: O(n) → fast
