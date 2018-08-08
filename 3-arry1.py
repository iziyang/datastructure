# coding:utf-8

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if numbers is None or len(numbers) <= 0:
            return False
        else:
            for i in numbers:
                if i < 0 or i > len(numbers) - 1:
                    return False
            for i in range(len(numbers)):
                while numbers[i] != i:
                    if numbers[i] == numbers[numbers[i]]:
                        duplication[0] = numbers[i]
                        return True
                    else:
                        index = numbers[i]
                        numbers[i], numbers[index] = numbers[index], numbers[i]
            return False


# if __name__ == '__main__':
#     num = [2, 1, 3, 1, 4]
#     duplication = [0]
#     s = Solution()
#     print s.duplicate(num, duplication)
