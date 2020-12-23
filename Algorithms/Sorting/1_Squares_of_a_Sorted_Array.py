# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
'''
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
'''
import time


class Solution:
    # all the methods below will cost O(n^2) to run
    def sortedSquares(self, nums: list) -> list:
        return sorted([a * a for a in nums])

    # def sortedSquares_naive(self, nums: list) -> list:
    #     c = [x ** 2 for x in nums]
    #     c.sort()
    #     return c

    # def sortedSquares_naive2(self, nums: list) -> list:
    #     if nums[0] >= 0:  # no negative values are in the list - O(n)
    #         return [x ** 2 for x in nums]
    #     elif nums[-1] < 0:  # worst case: every element is negative - O(n)
    #         print("Negative array")
    #         return [nums[i] ** 2 for i in range(len(nums) - 1, -1, -1)]
    #     else:
    #         length = len(nums)
    #         first_non_negative_index = length - 1  # in the worst case that the last element is positive
    #         result = []
    #         for i in range(length):
    #             if nums[i] >= 0:
    #                 first_non_negative_index = i
    #                 print("First non negative index >>>", first_non_negative_index)
    #                 break
    #         pos_index = first_non_negative_index
    #         neg_index = first_non_negative_index - 1
    #         while True:
    #             if pos_index >= length and neg_index <= -1:
    #                 break
    #
    #             if pos_index >= length:
    #                 result.append(nums[neg_index] ** 2)
    #                 neg_index -= 1
    #             elif neg_index <= -1:
    #                 result.append(nums[pos_index] ** 2)
    #                 pos_index += 1
    #             else:
    #                 pos_square = nums[pos_index] ** 2
    #                 neg_square = nums[neg_index] ** 2
    #                 if pos_square >= neg_square:
    #                     result.append(neg_square)
    #                     neg_index -= 1
    #                 else:
    #                     result.append(pos_square)
    #                     pos_index += 1
    #
    #         return result


if __name__ == '__main__':
    s = Solution()

    # arr = [1, 2, 3]
    # print(s.sortedSquares(arr))
    #
    # arr = [-4, -2, -1]
    # print(s.sortedSquares(arr))
    #
    # arr = [-1, 0, 1, 2, 3]
    # print(s.sortedSquares(arr))
    #
    # arr = [1, 2, 3]
    # print(s.sortedSquares(arr))
    #
    # arr = [-4, -2, -1]
    # print(s.sortedSquares(arr))
    #
    # arr = [-1, 0, 1, 2, 3]
    # print(s.sortedSquares(arr))
