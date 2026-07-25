class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        ops = {
            "*": lambda a, b: a * b,
            "/": lambda a, b: math.trunc(a / b),
            "-": lambda a, b: a - b,
            "+": lambda a, b: a + b,
        }

        # popleft, popleft -> 1 + 2
        # append -> [3]
        for token in tokens:
            op = ops.get(token)
            if op is None:  # it's an operand
                operand = int(token)
                stack.append(operand)
                continue
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = op(operand1, operand2)
            stack.append(result)

        return stack.pop()
