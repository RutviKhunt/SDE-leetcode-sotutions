intervals.sort(key=lambda x: (x[1], -x[0]))
        
        result = 0
        a = b = -1  # last two selected numbers
        
        for s, e in intervals:
            cnt = 0
            
            # Count how many of (a, b) are inside [s, e]
            if a >= s:
                cnt += 1
            if b >= s:
                cnt += 1
            
            # If two already covered, continue
            if cnt >= 2:
                continue
            
            # If only one covered → add one more
            if cnt == 1:
                result += 1
                # Add biggest possible not in set
                if a >= s:
                    # add e
                    b = e
                else:
                    # add e
                    b = e
                    a = b - 1
            else:
                # Add two numbers: e-1, e
                result += 2
                a = e - 1
                b = e
        
        return result