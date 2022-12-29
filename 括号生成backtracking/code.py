"""
使用递归方法先加一个左括号，然后依次尝试加一个左括号或加一个右括号，如果右边括号数量大于左边则是无效括号直接返回，知道最后左括号数量和右括号数量和n都相等则代表这是一个有效括号，添加到list中即可

作者：ffchic
链接：https://leetcode.cn/problems/generate-parentheses/solution/di-gui-shi-xian-by-clever-chateletxrp-9ycz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
def backtracking(n, result, left, right, str):
    """
    :param result: 要返回的list
    :param left: 左边括号的数量
    :param right: 右边括号的数量
    :param str: 括号拼接的字符串
    :return:
    """
    if right > left:
        return
    elif right == left == n:
        result.append(str)
        return
    if left < n:
        backtracking(n, result, left+1, right, str+"(")
    if right < left:
        backtracking(n, result, left,right+1,str+")")



class Solution:
    def generateParenthesis(self, n):
        result = []
        backtracking(n, result, 0, 0, '')
        return result

s = Solution()
print(s.generateParenthesis(3))