class Solution:

    #   0 1 2
    #   1 2 3

    #     1 0
    #     3 4

    # 0 1 2 3
    # 3 2 1 0
    # 4 1 8 2
    @staticmethod
    def multiplyStrings(num1: str, num2: str) -> str:
        lower = num1
        upper = num2

        if len(lower) > len(upper):
            lower = num2
            upper = num1

        res = [0 for _ in range(0, len(upper) + len(lower))]

        transit = 0
        for l_i, l_e in (list(enumerate(reversed(lower)))):
            for u_i, u_e in (list(enumerate(reversed(upper)))):
                mul = int(l_e) * int(u_e)
                curr_res = mul + transit + res[l_i + u_i]

                if curr_res >= 10:
                    transit = curr_res // 10
                    curr_res = curr_res - transit * 10
                else:
                    transit = 0

                res[l_i + u_i] = curr_res


        return ''.join(map(str, reversed(res)))


def main():
    # assert Solution.multiplyStrings(str(123), str(2)) == '246'  # simplest case
    # assert Solution.multiplyStrings(str(123), str(4)) == '492'  # simplest case
    # assert Solution.multiplyStrings(str(123), str(34)) == '4182'  # simplest case
    # assert Solution.multiplyStrings(str(1234), str(456)) == '562704'  # simplest case
    assert Solution.multiplyStrings(str(33), str(33)) == '56088'  # simplest case
    assert Solution.multiplyStrings(str(123), str(456)) == '56088'  # simplest case


if __name__ == "__main__":
    main()
