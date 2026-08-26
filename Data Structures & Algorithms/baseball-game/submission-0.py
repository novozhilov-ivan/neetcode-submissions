class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op.is_digit():
                stack.append(int(rec))
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            if op == "C":
                stack.pop()
            if op == "D":
                stack.append(2 * stack.pop())
        
        return sum (stack)

        

