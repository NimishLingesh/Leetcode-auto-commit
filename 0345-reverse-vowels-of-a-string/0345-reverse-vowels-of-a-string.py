class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v_stack = []
        for ch in s:
            if ch in vowels:
                v_stack.append(ch)
        s_list = list(s)
        for idx, ch in enumerate(s_list):
            if ch in vowels:
                c = v_stack.pop(-1)
                s_list[idx] = c
        return ''.join(e for e in s_list)