class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # positions of zeros
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        zlen = len(zeros)

        # Case k = 0: substrings with zero zeros => all-ones runs
        ans = 0
        run = 0
        for ch in s:
            if ch == '1':
                run += 1
            else:
                ans += run * (run + 1) // 2
                run = 0
        ans += run * (run + 1) // 2

        # LIMIT for zeros count
        import math
        LIMIT = int(math.sqrt(n)) + 1

        # For each k from 1..LIMIT, count substrings having exactly k zeros
        for k in range(1, LIMIT + 1):
            if k > zlen:
                break
            minLen = k * k + k  # minimum substring length needed: ones + zeros >= k^2 + k

            # iterate over consecutive zero-blocks of length k
            for i in range(0, zlen - k + 1):
                j = i + k - 1  # zeros[i..j] are the k zeros included

                # left choices range: from Lmin to Lmax (inclusive)
                Lmin = 0 if i == 0 else zeros[i - 1] + 1
                Lmax = zeros[i]

                # right choices range: from Rmin to Rmax (inclusive)
                Rmin = zeros[j]
                Rmax = n - 1 if j == zlen - 1 else zeros[j + 1] - 1

                # quick check: maximum possible length with best left and right
                max_possible_len = Rmax - Lmin + 1
                if max_possible_len < minLen:
                    continue  # no possible substring for this block

                # left must satisfy: left <= Lmax and left <= Rmax - (minLen - 1)
                left_upper = min(Lmax, Rmax - (minLen - 1))
                if left_upper < Lmin:
                    continue

                # split left range into two parts:
                # part A: left where left + minLen -1 <= Rmin  => right_low = Rmin
                # i.e., left <= Rmin - (minLen - 1)
                left_split = Rmin - (minLen - 1)
                A_lo = Lmin
                A_hi = min(left_upper, left_split)

                if A_hi >= A_lo:
                    numA = A_hi - A_lo + 1
                    cnt_right_for_A = (Rmax - Rmin + 1)
                    ans += numA * cnt_right_for_A

                # part B: left where left > left_split up to left_upper
                B_lo = max(Lmin, left_split + 1)
                B_hi = left_upper
                if B_hi >= B_lo:
                    # for left in [B_lo..B_hi], right_low = left + minLen - 1
                    # contribution = sum_{L=B_lo..B_hi} (Rmax - (L + minLen -1) + 1)
                    # = sum_{L=B_lo..B_hi} (Rmax - minLen - L + 2)
                    count = B_hi - B_lo + 1
                    # sum of L from B_lo..B_hi = (B_lo + B_hi) * count // 2
                    sumL = (B_lo + B_hi) * count // 2
                    contrib = count * (Rmax - minLen + 2) - sumL
                    ans += contrib

        return ans