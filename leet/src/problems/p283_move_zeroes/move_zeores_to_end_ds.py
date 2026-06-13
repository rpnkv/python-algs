from typing import List


class Solution:
    def moveZeroesInv(self, nums: List[int]) -> None:
        write = 0
        n = len(nums)

        print()
        for read in range(n):
            print(f"nums before loop {nums}")
            # === ЗДЕСЬ, ПЕРЕД ИТЕРАЦИЕЙ, ДОЛЖНЫ ВЫПОЛНЯТЬСЯ ИНВАРИАНТЫ ===
            # Инвариант 1: nums[0:write] - ненулевые в правильном порядке.
            # (Используем срез [0:write], что соответствует nums[0..write-1])
            # Проверим, что все элементы в этом срезе ненулевые.
            # Если write == 0, срез пуст - проверка тривиально истинна.
            if write > 0:
                assert all(num != 0 for num in nums[0:write]), f"Inv1 failed at read={read}, write={write}"

            # Инвариант 2: nums[write:read] - только нули.
            # (Срез [write:read] соответствует nums[write..read-1])
            # Если write >= read, срез пуст.
            if write < read:
                assert all(num == 0 for num in nums[write:read]), f"Inv2 failed at read={read}, write={write}"
            # ==============================================================
            # ТЕЛО ЦИКЛА: что мы делаем на этой итерации?
            if nums[read] != 0:
                # Мы нашли ненулевой элемент nums[read]
                # По инварианту 2, nums[write] - это ноль (или write == read)
                # Меняем их местами
                nums[write], nums[read] = nums[read], nums[write]
                # Теперь nums[write] стал ненулевым (правильным элементом)
                # Сдвигаем write, чтобы указать на следующую позицию для будущего ненулевого элемента
                write += 1
            # Конец итерации. Переменная read увеличится сама в цикле for.
            print(f"nums after loop  {nums}")
            print()
        print(f"nums finally {nums}")
        # После цикла read == n
        # Что говорят инварианты в этот последний момент?
        # Инвариант 1: nums[0:write] - все ненулевые в порядке.
        # Инвариант 2: nums[write:n] - все нули. (т.к. read == n)
        # Это и есть требуемый результат!

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]  # swap
                write += 1
