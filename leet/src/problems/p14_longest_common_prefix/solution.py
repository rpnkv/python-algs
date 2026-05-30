class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = strs[0]

        for s in strs[1:]:
            if len(s) < len(shortest_str):
                shortest_str = s

        for i in range(len(shortest_str)):
            for s in strs:
                if s[i] != shortest_str[i]:
                    return shortest_str[:i]

        return shortest_str