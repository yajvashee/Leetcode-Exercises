class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        number_occurence = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] not in number_occurence:
                    number_occurence[grid[i][j]] = 1
                else:
                    number_occurence[grid[i][j]] += 1
        print(number_occurence)
        for i in range(1,(len(grid) ** 2) + 1):
            if i not in number_occurence:
                b = i
            elif number_occurence[i] == 2:
                a = i
            
        ans.append(a)
        ans.append(b)
        return ans