def kmp_search(txt: str, ptn: str) -> int:
    txt_p = 1
    ptn_p = 0
    skip_arr = [0] * (len(ptn)+1)

    while txt_p != len(ptn):
        if ptn[txt_p] == ptn[ptn_p]:
            txt_p += 1
            ptn_p += 1
            skip_arr[txt_p] = ptn_p
        elif ptn_p == 0:
            txt_p += 1
            skip_arr[txt_p] = ptn_p
        else:
            ptn_p = skip_arr[ptn_p]
    
    txt_p = 0
    ptn_p = 0

    while txt_p != len(txt) and ptn_p != len(ptn):
        if txt[txt_p] == ptn[ptn_p]:
            txt_p += 1
            ptn_p += 1
        elif ptn_p == 0:
            txt_p += 1
        else:
            ptn_p = skip_arr[ptn_p]
    
    return txt_p - ptn_p if ptn_p == len(ptn) else -1


print(kmp_search("abcdef1234", "cd"))
print(kmp_search("abcdef1234", "f1"))
print(kmp_search("abcdef1234", "ac"))
print(kmp_search("abcdef1234", "def123"))