# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n, cache=None):
        if cache is None:
            cache = {}
        if n in cache:
            return cache[n]
        if n == 0:
            return 0
        if n == 1:
            return 1

        cache[n] = self.Fibonacci(n - 1, cache) + self.Fibonacci(n - 2, cache)
        return cache[n]

        # write code here

    def fibonacci_cache(self, n, cache=None):
        if cache is None:
            cache = {}
        if n in cache:
            return cache[n]
        if n <= 1:
            return 1
        cache[n] = self.fibonacci_cache(n - 1, cache) + self.fibonacci_cache(n - 2, cache)
        return cache[n]


s = Solution()
print s.fibonacci_cache(50)
print s.Fibonacci(100)
