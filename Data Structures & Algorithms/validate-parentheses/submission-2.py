class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "}": "{", "]": "["}

        stack = []

        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)

            elif i in d:
                if not stack or d[i] != stack[-1]:
                    return False

                stack.pop()

        return not stack