class Solution:  # looks like it may be refactored
    positive_boundary = pow(2, 31) - 1
    negative_boundary = pow(-2, 31)

    def reverse(self, x: int) -> int:

        # int number = 0

        num_str = str(x)
        target_str = "0"

        if x > 0:
            if len(num_str) <= len(str(self.positive_boundary)):
                for i in range(len(num_str) - 1, -1, -1):
                    target_str = target_str + num_str[i]

            int_target = int(target_str)
            if int_target > self.positive_boundary:
                return 0
            else:
                return int_target
        else:
            if len(num_str) <= len(str(self.negative_boundary)):
                for i in range(len(num_str) - 1, 0, -1):
                    target_str = target_str + num_str[i]

            if target_str != "":
                target_str = "-" + target_str

            int_target = int(target_str)
            if int_target < self.negative_boundary:
                return 0
            else:
                return int_target
