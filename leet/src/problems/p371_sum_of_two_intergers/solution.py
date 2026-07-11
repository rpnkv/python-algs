class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        mask = 0b01

        carry = 0

        while a or b or carry:
            #res = res << 1
            a_bit = a & mask
            b_bit = b & mask

            if a_bit & b_bit & carry:
                carry = 0b01
                res_mask = 0b01
            elif a_bit & b_bit:
                carry = 0b01
                res_mask = 0b00
            elif (a_bit | b_bit) & carry:
                carry = 0b01
                res_mask = 0b00
            elif a | b_bit | carry:
                carry = 0b00
                res_mask = 0b01
            else:
                carry = 0b00
                res_mask = 0b00

            #res = res | res_mask
            res |= (1 << i)

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