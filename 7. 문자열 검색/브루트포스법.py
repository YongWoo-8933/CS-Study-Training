def brute_force_search(txt: str, ptn: str) -> int:
    txt_p = 0
    ptn_p = 0

    while txt_p != len(txt) and ptn_p != len(ptn):
        if txt[txt_p] == ptn[ptn_p]:
            txt_p += 1
            ptn_p += 1
        else:
            txt_p = txt_p - ptn_p + 1
            ptn_p = 0
    
    return txt_p - ptn_p if ptn_p == len(ptn) else -1

print(brute_force_search("abcdef1234", "cd"))
print(brute_force_search("abcdef1234", "f1"))
print(brute_force_search("abcdef1234", "ac"))
print(brute_force_search("abcdef1234", "def123"))