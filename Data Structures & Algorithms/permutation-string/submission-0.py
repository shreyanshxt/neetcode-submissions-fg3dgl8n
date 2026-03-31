class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        count = {}

        # frequency of s1
        for c in s1:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        window_size = len(s1)
        r = window_size

        while r <= len(s2):

            window = s2[l:r]
            count2 = {}

            for f in range(len(window)):
                if window[f] in count2:
                    count2[window[f]] += 1
                else:
                    count2[window[f]] = 1

            if count == count2:
                return True

            l += 1
            r += 1

        return False