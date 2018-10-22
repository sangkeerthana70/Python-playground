def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    return compare_lists(tokenize(a,n),tokenize(b,n))

def tokenize(s,n):
    result = []
    for i in range(len(s)-n+1):
        token = s[i:i+n]
        if not token in result:
            result.append(token)
    return result

def compare_lists(list1,list2):
    result = []
    for la in list1:
        for lb in list2:
            if la == lb and la not in result:
                result.append(la)
    return result


