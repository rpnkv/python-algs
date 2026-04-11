from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def to_minutes(event_str: str) -> int:
            hours, minutes = event_str.split(':')

            return int(minutes) + int(hours) * 60

        events_ints=[[to_minutes(timestamp) for timestamp in event1], [to_minutes(timestamp) for timestamp in event2]]
        events_ints.sort(key=lambda lst: lst[0])

        first_starting = events_ints[0]
        second_starting = events_ints[1]

        if first_starting[0] == second_starting[0]: # start time same
            return True

        if second_starting[0] <= first_starting[1]:
            return True


        return False