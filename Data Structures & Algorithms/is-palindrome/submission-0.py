class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                ch = ch.lower()
                cleaned += ch

        return cleaned == cleaned[::-1]