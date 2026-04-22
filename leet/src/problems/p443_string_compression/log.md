# a cold attempt
two pointers
left points to the beginning of current substring with same characters
right iterates

at each iteration, we must determine, whether new character belongs to prev string (at l pos) or to new.
in first case, we just iterate letters counter
in second (new letter discovered) -- commit prev count, shift left pointer, initialize new count

# didnt' work, improving my solution
итерируемся по списку символов. нужно хранить длинну текущей серии и начальный символ, чтобы не "потеряться"
при итерировании.
компактнее всего хранить позицию первого символа предыдущей серии на момент начала итерации
в конце итерации мы решаем: или "сбрасываем" состояние, или "продолжаем"
                                                                         
# didn't get the task description properly, re-making
