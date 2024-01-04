def find(lst: list[str], val: str, start_index=0) -> int:
    for i in range(start_index, len(lst)):
        if (lst[i]) == val:
            return i

    return -1


def remove_spaces(char_list: list[str]) -> list[str]:
    start_pointer = find(char_list, ' ', 0)

    if start_pointer != -1:
        for i in range(start_pointer + 1, len(char_list)):
            if char_list[i] != ' ':
                char_list[start_pointer] = char_list[i]
                start_pointer += 1

    else:
        return char_list

    return char_list[:start_pointer]


if __name__ == '__main__':
    assert remove_spaces(list("superproposition")) == list("superproposition")
    assert remove_spaces(list("s  upe rpropos   ition")) == list("superproposition")
    assert remove_spaces(list("   superproposition   ")) == list("superproposition")
    assert remove_spaces(list(" superproposition   ")) == list("superproposition")
    assert remove_spaces(list("  s  uperpr  oposition ")) == list("superproposition")
    assert remove_spaces(list("s  uperpr           oposition ")) == list("superproposition")
    assert remove_spaces(list("  supe rpropos   ition ")) == list("superproposition")
    assert remove_spaces(list("      ")) == list("")
    print("гузеля ты самая лучшая\n"
          "спасибо")