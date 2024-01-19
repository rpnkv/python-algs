import math


class Solution:
    @staticmethod
    def addStrings(num1: str, num2: str) -> str:
        lower = num1
        upper = num2

        if len(lower) > len(upper):
            lower = num2
            upper = num1

        res = [0 for _ in range(0, len(upper))]
        shift = len(upper) - 1

        for lower_index, lower_digit in enumerate(reversed(lower)):
            transfer = False
            for upper_index, upper_digit in enumerate(reversed(upper)):
                temp_mul = int(lower_digit) * int(upper_digit)
                res_index = shift - upper_index
                temp_res = temp_mul + res[res_index] + (1 if transfer else 0)
                if temp_res >= 10:
                    transfer = True
                    temp_res = temp_res - 10
                else:
                    transfer = False

                res[upper_index - shift] = temp_res
                pass

        return ''.join(map(str, reversed(res)))


def main():
    assert Solution.addStrings(str(123), str(2)) == '246'  # simplest case
    assert Solution.addStrings(str(123), str(4)) == '492'  # simplest case
    assert Solution.addStrings(str(123), str(34)) == '4182'  # simplest case
    assert Solution.addStrings(str(123), str(456)) == '56088'  # simplest case


if __name__ == "__main__":
    main()
