class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer = []
        for i,price in enumerate(prices):
            if i == len(prices) - 1:
                answer.append(price)
            elif min(prices[i+1:]) > prices[i]:
                answer.append(price)
            else:
                for j in range(i+1,len(prices)):
                    if prices[j] <= prices[i]:
                        answer.append(prices[i] - prices[j])
                        break
                    continue
        return answer
