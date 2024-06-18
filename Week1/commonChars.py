class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        output = []
        for c in set(words[0]):
            minimum = words[0].count(c)
            for i in range(1, len(words)):
                a = words[i].count(c)
                if a<minimum:
                    minimum = a
            for i in range(minimum):
                output.append(c)

        return output
