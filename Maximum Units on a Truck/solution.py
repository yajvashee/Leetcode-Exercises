class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        total = 0
        boxTypes.sort(key = lambda x:x[1],reverse = True)
        print(boxTypes)
        for item in boxTypes:
            print(truckSize,item[0])
            if item[0] < truckSize:
                total+=item[0] * item[1]
                truckSize -=item[0]
            else:
                total += item[1] * truckSize
                break
        return total