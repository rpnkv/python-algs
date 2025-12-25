from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        В этой реализации у нас 3 зоны:
        - по левую сторону от левого -- не подлежащие удалению;
        - между левым и правым "серая зона"?;
        - по правую сторону от правого -- не проверенные.

        Что меня смущает? Почему мы слепо двигаем элементы на левый указатель, если они не "удаляемые"?
        
        """

        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left