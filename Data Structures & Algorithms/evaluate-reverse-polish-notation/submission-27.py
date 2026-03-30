class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                digit2 = stack.pop()
                digit1 = stack.pop()

                if token == '+':
                    stack.append(digit1 + digit2)
                elif token == '-':
                    stack.append(digit1 - digit2)
                elif token == '*':
                    stack.append(digit1 * digit2)
                elif token == '/':
                    stack.append(int(digit1 / digit2))  # truncates toward 0

        return stack[-1]