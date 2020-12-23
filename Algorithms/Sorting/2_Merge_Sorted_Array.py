# Link: https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0  # to change the element of nums 1
        index1 = index2 = 0
        copy_nums1 = nums1.copy()
        while index < len(nums1):
            if index1 >= m and index2 >= n:
                break
            elif index1 >= m:
                nums1[index: m + n] = nums2[index2:n]
                break
            elif index2 >= n:
                nums1[index: m + n] = copy_nums1[index1:m]
                break
            else:
                number1 = copy_nums1[index1]
                number2 = nums2[index2]
                if number1 >= number2:
                    nums1[index] = number2
                    index2 += 1
                else:
                    nums1[index] = number1
                    index1 += 1

            # print(nums1)
            index += 1


if __name__ == '__main__':
    print("Merge Sorted Array")
    s = Solution()

    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    # s.merge(nums1, m, nums2, n)
    # print(nums1)

    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)
