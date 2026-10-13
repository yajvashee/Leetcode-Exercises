class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s_groups = []
            number_of_groups = (len(s) + (k-1)) // k
            s_groups = [None] * number_of_groups
            for i in range(number_of_groups):
                if i != number_of_groups - 1:
                    s_groups[i] = s[i * k : (i+1) * k]
                else:
                    s_groups[i] = s[i*k:]
            for num in s_groups:
                digits_sum = sum(map(int, num))
                new_s_groups.append(digits_sum)
            s = "".join(map(str, new_s_groups))
            print(s)
        return str(s)
