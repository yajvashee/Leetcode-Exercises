class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        departure = set()
        arrival = set()
        for path in paths:
            departure.add(path[0])
            arrival.add(path[1])
        return list(arrival - departure)[0]