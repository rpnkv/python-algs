def main():
    arr1 = [1, 2, 4]
    arr2 = [6, 7]

    del arr2

    for i in range(len(arr1), 0, -1):
        print(i)


if __name__ == '__main__':
    main()
