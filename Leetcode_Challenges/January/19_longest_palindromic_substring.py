def is_palindrome(s: str) -> bool:  # Time Complexity => O(N)
    return s == s[::-1]


class Solution:
    def brute_longestPalindrome(self, s: str) -> str:  # Time Complexity => O(N^3)
        longest_len = 0
        longest_sub = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                cur_sub = s[i:j+1]
                # worst case -> longest_len not changed to a value bigger than 1,
                # so we have to check for palindrome [is_palindrome o(n)] for every sub
                if len(cur_sub) > longest_len and is_palindrome(cur_sub):
                    longest_len = len(cur_sub)
                    longest_sub = cur_sub
        return longest_sub

    def longestPalindrome(self, s: str) -> str:
        pass