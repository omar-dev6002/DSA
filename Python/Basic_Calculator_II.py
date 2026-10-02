class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'

        s += '+'

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch in "+-*/":
                if sign == "+":
                    stack.append(num)

                elif sign == "-":
                    stack.append(-num)

                elif sign == "*":
                    prev = stack.pop()
                    stack.append(prev * num)

                elif sign == "/":
                    prev = stack.pop()
                    stack.append(int(prev / num))

                sign = ch

                num = 0

        return sum(stack)


# Time: O(n)
# Space: O(n)
# See you soon🤗






