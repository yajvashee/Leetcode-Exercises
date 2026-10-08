class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        for i,char in enumerate(s):
            if i == 0 and char == '?':
                if s[i+1] == '?':
                    s[i] = '1'
                elif int(s[i+1]) > 1:
                    s[i] = '0'
                else:
                    s[i] = '1'
            if i == 1 and char == '?':
                if int(s[i-1]) == 0:
                    s[i] = '9'
                else:
                    s[i] = '1'
            if i == 3 and char == '?':
                s[i] = '5'
            if i == 4 and char =='?':   
                s[i] = '9'
        print(s)
        delimiter = ""
        return delimiter.join(s)
                