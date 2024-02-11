def caesarCipher(s, k):
    out = []
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        if i.islower():
            x = (lower.index(i) + k) % 26
            out.append(lower[x])
        elif i.isupper():
            y = (upper.index(i) + k) % 26
            out.append(upper[y])
        else:
            out.append(i)
    return ''.join(out)