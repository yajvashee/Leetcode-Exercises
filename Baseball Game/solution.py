class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []
        for op in operations:
            if op not in ['C','D','+']:
                scores.append(int(op))
            elif op == 'C':
                scores.pop()
            elif op == 'D':
                last = scores[-1]
                scores.append(2 * int(last))
            else:
                scores.append(int(scores[-1]) + int(scores[-2]))
        return sum(scores)