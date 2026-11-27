class Solution:
    def fillCups(self, amount: list[int]) -> int:
        count = 0
        while amount != [0,0,0]:
            print(amount)
            count +=1
            max_amount = max(amount)
            min_amount = min(amount)
            if min_amount == 0:
                return count + max_amount - 1
            max_found = False
            min_found = False
            for i,a in enumerate(amount):
                if a == max_amount and max_found == False:
                    max_found = True
                    max_index = i
                else:
                    if a == min_amount and min_found == False and a!=0:
                        min_found = True
                        min_index = i
            amount[max_index] -=1
            amount[min_index] -= 1
        return count
                