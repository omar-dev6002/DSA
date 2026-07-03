class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            # If the token is an operator, pop two elements and calculate
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Python's default integer division (//) rounds towards negative infinity.
                    # LeetCode 150 specifically requires truncation towards zero.
                    # Using int(a / b) achieves the correct behavior for negative numbers.
                    stack.append(int(a / b))
            else:
                # If it's a number, convert to integer and push to stack
                stack.append(int(token))
                
        # The final result is the only remaining element in the stack
        return stack[0]
