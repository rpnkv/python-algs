from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # two pointers
        # left points to the beginning of current substring with same characters
        # right iterates

        # at each iteration, we must determine, whether new character belongs to prev string (at l pos) or to new.
        # in first case, we just iterate letters counter
        # in second (new letter discovered) -- commit prev count, shift left pointer, initialize new count

        # improving my solution, pt1.
        # итерируемся по списку символов. нужно хранить длинну текущей серии и начальный символ, чтобы не "потеряться"
        # при итерировании.
        # компактнее всего хранить позицию первого символа предыдущей серии на момент начала итерации
        # в конце итерации мы решаем: или "сбрасываем" состояние, или "продолжаем"
        #

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