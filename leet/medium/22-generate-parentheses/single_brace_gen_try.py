def generate(n: int, curr: int, acc: str) -> str:
    if curr != n:
        return generate(n, curr + 1, acc + ')')
    else:
        return acc


def main():
    print(generate(5, 0, ''))


if __name__ == '__main__':
    main()
