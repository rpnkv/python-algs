# проверка должна быть после изменения стейта: в текущем цикле, или в следующем
def generate(n: int, curr: int, acc: str) -> str:
    if curr == n:
        return acc
    else:
        return generate(n, curr + 1, acc + ')')


def main():
    assert generate(5, 0, '') == ')))))'


if __name__ == '__main__':
    main()
