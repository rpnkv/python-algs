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
            trans = False
            for index, letter in enumerate(num1):
                sum = int(letter) + int(num2[index]) + (1 if trans else 0)
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
    assert Solution.addStrings(str(3), str(3)) == '6'  # simplest case
    assert Solution.addStrings(str(33), str(33)) == '66'  # +1 position
    assert Solution.addStrings(str(23), str(23)) == '46'  # +1 position
    assert Solution.addStrings(str(3), str(7)) == '10'  # +1 carry
    assert Solution.addStrings(str(4), str(7)) == '11'  # +1 more complex carry
    assert Solution.addStrings(str(14), str(7)) == '21'  # +1 more complex carry + position
    assert Solution.addStrings(str(456), str(77)) == '533'  # +1 more complex carry + position
    assert Solution.addStrings(str(123456789), str(987654321)) == '1111111110'  # +1 more complex carry + position


if __name__ == "__main__":
    main()
