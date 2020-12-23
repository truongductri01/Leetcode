# Link: https://leetcode.com/problems/valid-palindrome/

# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
'''
Questions:
    1. Should we strip the whitespace and special character away?
        No because the process will cost O(n) time to loop through and clean up

Idea:
    Start from the two end and control the process using left_index, right_index
        If left_index > right_index: end the process
    while left_index <= right_index:
        if the character at that index is not an alphanumeric characters
            => increase the index of that side
        else:
            compare the characters, return False if not the same
            else: increase left_index and decrease the right_index

    Time complexity: O(n)

Is there a way to reduce the time? O(n) to O(n*log(n)) or O(1)?
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s) - 1
        while left_index <= right_index:
            if not s[left_index].isalnum():
                left_index += 1
            elif not s[right_index].isalnum():
                right_index -= 1
            else:
                if s[left_index].lower() != s[right_index].lower():
                    return False
                else:
                    left_index += 1
                    right_index -= 1
        return True


if __name__ == '__main__':
    print("Valid Palindrome")
    s = Solution()

    string = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(string))

    string = "race a car"
    print(s.isPalindrome(string))