class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1


        i = 0
        n = len(s)

        sign = 1
        result = 0

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == "-":
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit 

            number = sign * result

            if number < INT_MIN:
                return INT_MIN
            if number > INT_MAX:
                return INT_MAX
            
            i += 1
        return sign * result



# Time Complexity: O(n)
# Space Complexity: O(1)
# See you soon 🤗
