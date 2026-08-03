class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_center, best_radius = 0, 0
        t = "#" + "#".join(s) + "#"
        radii = [0] * len(t)
        best_l, best_r = 0, 0

        for center, _ in enumerate(t):
            if center < best_r:
                radii[center] =

            radius = radii[center]
            l = r = center

            while (l >= 0 and r < len(t) and
                   t[l] == t[r]):
                radius += 1
                l, r = l - 1, r + 1

            radius -= 1

            if radius > best_radius:
                best_center, best_radius = center, radius

        start = (best_center - best_radius) // 2
        length = best_radius

        return s[start:start + length]
