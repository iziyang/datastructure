# coding:utf-8


class Solution:

    def count_range(self, numbers, length, start, end):
        if numbers is None:
            return False
        count = 0
        for i in range(0, length):
            if start <= numbers[i] <= end:
                count += 1
        return count  # 返回区间的数目

    def getDuplication(self, numbers, length):
        if numbers is None or len(numbers) <= 0:
            return False
        else:
            start = 1  # 1
            end = length - 1  # n
            while end >= start:
                middle = ((end - start) >> 1) + start
                count = self.count_range(numbers, length, start, middle)
                if end == start:
                    if count > 1:
                        return start
                    else:
                        break
                if count > (middle - start + 1):
                    end = middle
                else:
                    start = middle + 1
            return False


# 测试
if __name__ == '__main__':
    num = [2, 3, 5, 4, 3, 2, 6, 7]
    s = Solution()
    print s.getDuplication(num, 8)
