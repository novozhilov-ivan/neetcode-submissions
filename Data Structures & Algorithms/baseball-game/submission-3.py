class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            if op.isdigit():
                stack.append(int(op))
            if op == "C":
                stack.pop()
            if op == "D":
                stack.append(2 * stack.pop())
        
        return sum (stack)

        

