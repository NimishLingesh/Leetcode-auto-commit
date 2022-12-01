class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        first_half = 0
        for i in s[:len(s)//2]:
            if i in vowels:
                first_half += 1
        second_half = 0
        for i in s[len(s)//2:]:
            if i in vowels:
                second_half += 1
        return first_half == second_half