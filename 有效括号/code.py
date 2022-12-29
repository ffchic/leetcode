"""
解题思路
使用栈实现，遍历字符串，左括号入栈右括号和栈顶匹配是否是对应的括号
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not bool(self.items)


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            ')': '(',
            '}': '{',
            ']': '[' 
        }
        stack = Stack()
        for i in s:
            if i in ['(','{','[']:
                stack.push(i)
            else:
                if stack.is_empty():
                    return False
                if mapping.get(i) != stack.pop():
                    return False
        if not stack.is_empty():
            return False 
        return True