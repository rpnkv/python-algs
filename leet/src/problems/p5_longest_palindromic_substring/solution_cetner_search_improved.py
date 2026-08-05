class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#" + "#".join(s) + "#"
        best_center, best_radius = 0, 0

        for i in range(len(t)):
            radius = 0
            l = r = i
            while l >= 0 and r < len(t) and t[l] == t[r]:
                radius += 1
                l, r = i - radius, i + radius
            radius -= 1

            if best_radius < radius:
                best_center, best_radius = i, radius

        start = (best_center - best_radius) // 2
        return s[start: start + best_radius]
