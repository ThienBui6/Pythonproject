def reverse_String(s):
    hold = ""
    idx0 = 0
    idx1 = len(s) -1
    while idx0 < idx1:
        hold = s[idx0]
        s[idx0] = s[idx1]
        s[idx1] = hold
        idx0 += 1
        idx1 += 1 