# Link: https://leetcode.com/problems/valid-palindrome-ii
# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.

'''
Notes: the string will contains only alphabetic characters
Idea:
    Use the left_index and right_index to control the process of checking the palindrome
    But for this time, we need a counter, if counter is larger than 1 => return False
    In case the two characters are not the same
        Check if increase the left_index create the coincidence
        Check if decrease the right_index creates the coincidence

    tricky case: cupuupcu
        Then if we move the index of the left side up, then the program will return False
        Otherwise, if we move the index of the right side down, the program will return True

Runtime: 188 ms, faster than 25.76% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 14.5 MB, less than 66.94% of Python3 online submissions for Valid Palindrome II.
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s) - 1
        counter = 0
        while left_index <= right_index:
            if counter > 1:
                return False

            if s[left_index] != s[right_index]:
                if left_index + 1 >= right_index:  # just need to delete one character
                    return True
                elif s[left_index + 1] == s[right_index] and s[left_index + 2] == s[right_index - 1]:
                    left_index += 1
                    counter += 1
                elif s[left_index] == s[right_index - 1] and s[left_index + 1] == s[right_index - 2]:
                    right_index -= 1
                    counter += 1
                else:
                    return False
            else:
                left_index += 1
                right_index -= 1
        return True

    def cutString(self, s: str) -> str:
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            if s[left_index] != s[right_index]:
                return s[left_index: right_index + 1]
            else:
                left_index += 1
                right_index -= 1
        return ""


if __name__ == '__main__':
    print("Valid Palindrome")
    s = Solution()

    string = "abca"  # True
    print(s.validPalindrome(string))

    string = "abcbbcda"  # False
    print(s.validPalindrome(string))

    string = "cuppucu"  # should be True
    print(s.validPalindrome(string))
    # print(s.cutString(string))
