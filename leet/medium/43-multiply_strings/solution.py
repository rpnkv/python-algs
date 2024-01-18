import math


class Solution:
    @staticmethod
    def addStrings(num1: str, num2: str) -> str:
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))

        res = []

        if len(num1) < len(num2):
            num1 = num1 + ["0" for _ in range(0, len(num2) - len(num1))]
            pass

        if len(num2) < len(num1):
            num2 = num2 + ["0" for _ in range(0, len(num1) - len(num2))]
            pass

        if len(num2) == len(num1):
            trans = 0
            for index, letter in enumerate(num1):
                sum = int(letter) * int(num2[index]) + (1 if trans else 0)
                if sum >= 10:
                    res.append(sum - 10)
                    trans = True
                else:
                    res.append(sum)
                    trans = False
            if trans:
                res.append("1")

        return ''.join(map(str, reversed(res)))


def main():
    assert Solution.addStrings(str(2), str(3)) == '6'  # simplest case
    assert Solution.addStrings(str(3), str(6)) == '12'  # simplest case
    assert Solution.addStrings(str(12), str(12)) == '144'  # simplest case
    assert Solution.addStrings(str(123), str(456)) == '56088'  # simplest case


if __name__ == "__main__":
    main()
