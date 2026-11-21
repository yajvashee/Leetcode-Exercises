class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j or i+j == len(mat) - 1:
                    print(mat[i][j])
                    total += mat[i][j]
        return total