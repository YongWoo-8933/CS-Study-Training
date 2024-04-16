def b_m_search(txt: str, ptn: str) -> int:
    skip_arr = [0] * 256

    for txt_p in range(256):
        skip_arr[txt_p] = len(ptn)
    for txt_p in range(len(ptn)):
        skip_arr[ord(ptn[txt_p])] = len(ptn) - txt_p - 1
    
    while txt_p < len(txt):
        ptn_p = len(ptn) - 1
        while txt[txt_p] == ptn[ptn_p]:
            if ptn_p == 0:
                return txt_p
            txt_p -= 1
            ptn_p -= 1
        txt_p += max(skip_arr[ord(txt[txt_p])], len(ptn) - ptn_p)

    return -1


print(b_m_search("abcdef1234", "cd"))
print(b_m_search("abcdef1234", "f1"))
print(b_m_search("abcdef1234", "ac"))
print(b_m_search("abcdef1234", "def123"))