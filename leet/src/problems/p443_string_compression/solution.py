from typing import List


class Solution:

    def compress(self, chars: List[str]) -> int:
        output_str: list[str|int] = [chars[0]]

        for char in chars[1:]:
            if isinstance(output_str[-1], str):
                prev_char = output_str.pop()
                if char == prev_char:
                    output_str.append(char)
                    output_str.append(2)
                else:
                    output_str.append(prev_char)
                    output_str.append(char)
            else:
                curr_count = output_str.pop()
                prev_char = output_str.pop()
                if prev_char == char:
                    output_str.append(prev_char)
                    output_str.append(curr_count + 1)
                else:
                    output_str.append(prev_char)
                    output_str.append(curr_count)
                    output_str.append(char)

        chars.clear()
        for char in output_str:
            chars.append(str(char))


        return len(output_str)