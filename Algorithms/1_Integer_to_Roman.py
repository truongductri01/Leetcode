# Link: https://leetcode.com/problems/integer-to-roman/
'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''
import math
import random


class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ""
        else:
            exp = int(math.log10(num))
            largest = (num // (10 ** exp)) * 10 ** exp
            return self.transform(largest) + self.intToRoman(num % (10 ** exp))

    def transform(self, num: int) -> str:
        if num > 1000:  # is 1000, 2000, or 3000 only
            return "M" * (num // 1000)

        # Number will be in range of [1 - 10], [11 - 100], [101 - 1000], [1001 - 3999]
        array = [
            [1, "I"],
            [5, "V"],
            [10, "X"],
            [50, "L"],
            [100, "C"],
            [500, "D"],
            [1000, "M"]
        ]
        if num <= 10:
            base_index = 0
        elif num <= 100:
            base_index = 2
        else:
            base_index = 4

        base_unit = array[base_index]
        middle_unit = array[base_index + 1]
        max_unit = array[base_index + 2]

        max_number = max_unit[0]
        middle_number = middle_unit[0]
        base_number = base_unit[0]

        if num == max_number:
            return max_unit[1]
        elif num == max_number - base_number:
            return base_unit[1] + max_unit[1]
        elif num == middle_number:
            return middle_unit[1]
        elif num == middle_number - base_number:
            return base_unit[1] + middle_unit[1]
        else:
            if num < middle_number:
                return base_unit[1] * (num // base_number)
            else:
                return middle_unit[1] + base_unit[1] * ((num - middle_number) // base_number)

    def shorterWay(self, num) -> str:  # from other's code
        ans = ''
        while num > 0:
            if num >= 1000:
                ans += "M"
                num -= 1000
            elif num >= 900:
                ans += "CM"
                num -= 900
            elif num >= 500:
                ans += "D"
                num -= 500
            elif num >= 400:
                ans += "CD"
                num -= 400
            elif num >= 100:
                ans += "C"
                num -= 100
            elif num >= 90:
                ans += "XC"
                num -= 90
            elif num >= 50:
                ans += "L"
                num -= 50
            elif num >= 40:
                ans += "XL"
                num -= 40
            elif num >= 10:
                ans += "X"
                num -= 10
            elif num >= 9:
                ans += "IX"
                num -= 9
            elif num >= 5:
                ans += "V"
                num -= 5
            elif num >= 4:
                ans += "IV"
                num -= 4
            elif num >= 1:
                ans += "I"
                num -= 1
        return ans


if __name__ == '__main__':
    print()
    s = Solution()
    arr = [random.randint(1, 3999) for x in range(20)]
    for number in arr:
        print("number: {} >>>".format(number), s.intToRoman(number))
