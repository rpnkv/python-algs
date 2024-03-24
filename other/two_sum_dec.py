import itertools


class SumLoop:
    @staticmethod
    def resolve_number(num: list[str], index: int) -> int:
        if len(num) > index:
            return int(num[index])
        else:
            return 0

    @staticmethod
    def sum(num1: str, num2: str) -> list[int]:
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))

        result = []
        transfer = 0

        for i in range(max(len(num1), len(num2))):
            res = SumLoop.resolve_number(num1, i) + SumLoop.resolve_number(num2, i) + transfer

            if res - 10 >= 10:
                transfer = 1
                result.append(res)
            else:
                transfer = 0
                result.append(res)

        if transfer == 1:
            result.append(1)

        return list(reversed(result))


class SumIter:

    @staticmethod
    def sum(num1: str, num2: str):
        result = []
        shift = 0

        for tpl in itertools.zip_longest(reversed(num1), reversed(num2)):
            temp_sum = int(tpl[0] if tpl[0] is not None else "0") + int(tpl[1] if tpl[1] is not None else "0") + shift
            if temp_sum - 10 >= 10:
                shift = 1
                result.append(str(temp_sum - 10))
            else:
                shift = 0
                result.append(str(temp_sum))

        return ''.join(result)


def main():
    cases = {
        ("13", "123"): list(reversed(str((13 + 123))))
    }

    # print(SumLoop().sum("13", "123"))

    for case, sss in cases.items():
        assert SumIter.sum(case[0], case[1]) == sss


if __name__ == '__main__':
    main()
