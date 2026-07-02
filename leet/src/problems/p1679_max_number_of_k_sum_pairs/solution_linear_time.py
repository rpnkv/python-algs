
class Solution:
    # rev2
    def maxOperations(self, nums: List[int], k: int) -> int:
        s = set()
        count = 0

        for n in nums:
            target = k - n
            if target in s:
                count += 1
                s.remove(target)
            else:
                s.add(n)

        return count

if __name__ == "__main__":
    assert Solution().maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3) == 4