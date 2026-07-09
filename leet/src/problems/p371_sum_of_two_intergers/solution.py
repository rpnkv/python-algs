class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        mask = 0b01

        transfer = 0b00

        while a or b or transfer:
            res = res << 1
            a_mask = a & mask
            b_mask = b & mask

            if a_mask & b_mask & transfer:
                transfer = 0b01
                res_mask = 0b01
            elif a_mask & b_mask:
                transfer = 0b01
                res_mask = 0b00
            elif (a_mask | b_mask) & transfer:
                transfer = 0b01
                res_mask = 0b00
            elif a_mask | b_mask | transfer:
                transfer = 0b00
                res_mask = 0b01
            else:
                transfer = 0b00
                res_mask = 0b00

            res = res | res_mask
            a = a >> 1
            b = b >> 1

        return res


if __name__ == "__main__":
    cases = [
        #(1,2,3, "ex 1N"),
        (1,1,2, "ex 1L"),
        #(2,3,5, "ex 2")
    ]

    for i1, i2, e, case_id in cases:
        a = Solution().getSum(i1,i2)

        assert a == e, f"failed case {case_id}; a/e: {a}/{e}"