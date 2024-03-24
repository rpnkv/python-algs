def main():
    arr1 = [1, 2, 4]
    arr2 = [6, 7]

    del arr2

    for i in range(len(arr1) - 1, -1, -1):
        print(arr1[i])


if __name__ == '__main__':
    main()
