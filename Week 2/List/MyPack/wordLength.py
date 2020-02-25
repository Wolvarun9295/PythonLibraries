def spiltNCheck(n, str):
    length = []
    words = str.split(" ")
    for i in words:
        if len(i) > n:
            length.append(i)
    return length
