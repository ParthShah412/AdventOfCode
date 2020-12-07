f = open('input.txt','r')
lst = []
tmp_lst = []
for line in f:
    ans = line.strip('\n')
    if(ans == ''):
        lst.append(tmp_lst)
        tmp_lst = []
    else:
        tmp_lst.append(ans)
f.close()

def sol1(lst):
    cnt = 0
    for ele in lst:
        ch_lst = []
        for strn in ele:
            for ch in strn:
                if(ch not in ch_lst):
                    ch_lst.append(ch)
        cnt = cnt + len(ch_lst)
    return cnt

def find_common(str1, str2):
    dct1, dct2 = {}, {}
    for i in range(ord('a'), ord('z')+1):
        dct1[chr(i)], dct2[chr(i)] = 0,0
    for ele in str1:
        dct1[ele] = dct1[ele] + 1
    for ele in str2:
        dct2[ele] = dct2[ele] + 1
    
    eq_st = ''
    
    for i in range(ord('a'), ord('z')+1):
        if(dct1[chr(i)] != 0):
            if(dct1[chr(i)] == dct2[chr(i)]):
                eq_st = eq_st + chr(i)
    return eq_st

def sol2(lst):
    nw_cnt = 0

    for ele in lst:
        str1 = ele[0]
        for strn in ele[1:]:
            str1 = find_common(str1, strn)
        nw_cnt = nw_cnt + len(str1)
    return nw_cnt
sol1(lst), sol2(lst)
