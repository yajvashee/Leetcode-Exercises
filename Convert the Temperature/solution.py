class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ans = []
        ans.append(celsius + 273.15)
        ans.append(1.8 * celsius + 32)
        return ans