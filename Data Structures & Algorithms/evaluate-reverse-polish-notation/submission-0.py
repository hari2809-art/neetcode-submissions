class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            # If token is an operator
            if token in ["+", "-", "*", "/"]:

                # Pop last two numbers
                b = stack.pop()
                a = stack.pop()

                # Perform operation
                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                else:
                    # Division truncates toward zero
                    stack.append(int(a / b))

            # Number
            else:
                stack.append(int(token))

        return stack[0]