class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        if l1 < l2:
            l1, l2 = l2, l1
            str1, str2 = str2, str1

        if not str1.startswith(str2):
            return ''

        short = str2

        while l2 > 0:
            if l1 % l2 == 0:
                if str1 == short * (l1 // l2) and str2 == short * (len(str2) // len(short)):
                    return short

            l2 -= 1
            short = str2[:l2]
        
        return ''
