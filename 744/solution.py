from typing import List

# my ans:


def nextGreatestLetter(letters: List[str], target: str) -> str:
    ans = letters[0]
    for i in range(0, len(letters)):
        if letters[i] > target:
            if ans < target:
                ans = letters[i]
    return ans


print(nextGreatestLetter(["c", "f", "j"], "c"))
