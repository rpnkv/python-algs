from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int], val: int) -> int:
        """
        Two cycles:
            - external iterates left pointer;
            - internal iterates right pointer over repeating values;

        External:
            While current.next exists?
            Example: nums[1,2,3] len is 3. External cycle should break at 3, index of 3 is 2. So cycle invariant is:
            while external < len(nums).

        Internal:
            While current's next value exists and equals to current.
            - Example 1:
                State: nums[1,2,2] len is 3. External cycle should start at nums [1] break at nums[2] which is 2,
                    because there are no numbers in array.
                So: while ((internal < len(nums) - 1)  and nums[internal + 1] == nums[external + 1])
            - Example 2:
                State: nums[1,2,2,3] len is 4. External cycle should start at nums[1] and break at nums[2] which hs 2,
                    because nums[3] != nums[2].
                So: So: while ((internal < len(nums) - 1)  and nums[internal + 1] == nums[external + 1])
        """
        if len(nums) in (0, 1):
            return len(nums)

        external = 0
        internal = 1

        while external < len(nums):
            while (internal < len(nums) - 1) and nums[internal + 1] == nums[external + 1]:
                internal += 1
            nums[external + 1] = nums[internal]
            external += 1

        return external
