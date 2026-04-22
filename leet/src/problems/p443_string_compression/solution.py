from typing import List


class Solution:

    def __init__(self):
        self.output_str = ''
        self.current_count = 0
        self.l = 0

    def commit(self, chars: List[str]) -> None:
        if self.current_count == 1:
            self.output_str += chars[self.l]
        else:
            self.output_str += chars[self.l]
            self.output_str += str(self.current_count)

        self.current_count = 1

    def compress(self, chars: List[str]) -> int:
        for r, r_char in enumerate(chars):
            if r_char == chars[self.l]:
                self.current_count += 1
            else:
                self.commit(chars)
                self.l = r

        self.commit(chars)

        return len(self.output_str)