# -*- coding:utf-8 -*-

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s_list = list(s)
        s_replace = []
        for item in s_list:
            if item == ' ':
                s_replace.append('%')
                s_replace.append('2')
                s_replace.append('0')
            else:
                s_replace.append(item)
        return "".join(s_replace)