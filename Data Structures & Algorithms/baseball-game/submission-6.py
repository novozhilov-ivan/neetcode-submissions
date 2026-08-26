class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            if op == "D":
                stack.append(2 * stack[-1])
            if op == "C":
                stack.pop()
            if op.isdigit():
                stack.append(int(op))
        
        return sum (stack)

        

