def main():
    print('my name is', name())
    print('i love u bro')

def name(): 
    name = input('What is your name?')
    return name

# LeetCode Easy: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

# LeetCode Medium: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# LeetCode Hard: Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2, return the median of the two sorted arrays.
def find_median_sorted_arrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2
    if len(A) > len(B):
        A, B = B, A
    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2  # A
        j = half - i - 2  # B
        Aleft = A[i] if i >= 0 else float('-inf')
        Aright = A[i+1] if (i+1) < len(A) else float('inf')
        Bleft = B[j] if j >= 0 else float('-inf')
        Bright = B[j+1] if (j+1) < len(B) else float('inf')
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

# Example usage:
if __name__ == "__main__":
    print('Easy - Two Sum:', two_sum([2,7,11,15], 9))
    print('Medium - Longest Substring Without Repeating Characters:', length_of_longest_substring('abcabcbb'))
    print('Hard - Median of Two Sorted Arrays:', find_median_sorted_arrays([1,3], [2]))

main()

