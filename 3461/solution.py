# my approach
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) != 2:
            b = ""
            for i in range(0, len(s)-1):
                b = b+(str((int(s[i])+int(s[i+1])) % 10))

            return self.hasSameDigits(b)
        elif s[0] == s[1]:
            return True
        else:
            return False

# convinient approach


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [ord(c) - 48 for c in s]

        while len(digits) > 2:
            next_digits = [(digits[i] + digits[i+1]) %
                           10 for i in range(len(digits)-1)]
            digits = next_digits

        return len(digits) == 2 and digits[0] == digits[1]
