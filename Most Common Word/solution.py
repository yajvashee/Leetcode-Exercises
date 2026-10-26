class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        import string
        paragraph = paragraph.lower()
        paragraph = paragraph.replace('.', ' ')
        paragraph = paragraph.replace(',', ' ')
        translator = str.maketrans('', '', string.punctuation)
        paragraph = paragraph.translate(translator)
        paragraph = paragraph.split(' ')
        occurences = {}
        print(paragraph)
        for word in paragraph:
            if word in banned or word == '':
                continue
            else:
                if word not in occurences:
                    occurences[word] = 1
                else:
                    occurences[word] +=1
        return max(occurences,key=occurences.get)
        