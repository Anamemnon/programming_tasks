class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1:
            return s

        lst = list(s)
        p1 = 0
        p2 = len(s) - 1

        vowels = ['a', 'e', 'i', 'o', 'u']

        while p1 < p2:
            if lst[p1].lower() not in vowels:
                p1 += 1
            if lst[p2].lower() not in vowels:
                p2 -= 1

            if lst[p1].lower() in vowels and lst[p2].lower() in vowels:
                lst[p1], lst[p2] = lst[p2], lst[p1]
                p1 += 1
                p2 -= 1
        return ''.join(lst)
