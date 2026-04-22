from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        output_str = ""
        current_count = l = 0

        for r, r_char in enumerate(chars):
            if r_char == chars[l]:
                current_count += 1
            else:
                if current_count == 1:
                    output_str += chars[l]
                else:
                    output_str += chars[l]
                    output_str += str(current_count)

                current_count = 1
                l = r

        if current_count == 1:
            output_str += chars[l]
        else:
            output_str += chars[l]
            output_str += str(current_count)

        return len(output_str)