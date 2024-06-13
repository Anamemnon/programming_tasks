from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) <= 1:
            return s

        stack = deque([s[0]])

        for v in s[1:]:
            if v == '*' and stack and stack[-1] != '*':
                stack.pop()
            else:
                stack.append(v)
        return ''.join(stack)
