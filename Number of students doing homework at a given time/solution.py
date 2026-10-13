class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        count = 0
        times = []
        for i in range(len(startTime)):
            times = list(range(startTime[i],endTime[i]+1))
            if queryTime in times:
                count+=1
        return count