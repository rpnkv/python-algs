def resolve_number(num: str, index: int) -> int:
    if len(num) > index:
        return int(num[index])
    else:
        return 0


def sum(num1: str, num2: str) -> str:
    num1 = list(reversed(num1))
    num2 = list(reversed(num2))

    result = []
    transfer = 0

    for i in range(max(len(num1), len(num2))):
        res = resolve_number(num1, i) + resolve_number(num2, i) + transfer

        if res - 10 >= 10:
            transfer = 1
            result.append(res)
        else:
            transfer = 0
            result.append(res)


    if transfer == 1:
        result.append(1)

    return list(reversed(result))


def main():
    print(sum("13", "123"))


if __name__ == '__main__':
    main()
