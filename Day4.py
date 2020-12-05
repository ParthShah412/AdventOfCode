f = open('input.txt','r')
lst = []
dct = {}
max_len = 0
for line in f:
    tmp_lst = line.split(' ')
    tmp_lst[-1] = tmp_lst[-1].strip('\n')
    for ele in tmp_lst:
        ele_lst = ele.split(':')
        if len(ele_lst) == 1:
            if(len(dct.keys())>max_len):
                max_len = len(dct.keys())
            lst.append(dct)
            dct = {}
        else:
            dct[ele_lst[0]] = ele_lst[1]
f.close()

def valid_pass(ele):
    
    vld = False
    brth = int(ele['byr'])
    if(brth>=1920 and brth<=2002):
        iyr = int(ele['iyr'])
        if(iyr>=2010 and iyr<=2020):
            eyr = int(ele['eyr'])
            if(eyr>=2020 and eyr<=2030):
                hgt_ms, hgt = ele['hgt'][-2:], int(ele['hgt'][:-2])
                flg = False
                if(hgt_ms=='cm'):
                    if(hgt>=150 and hgt <=193):
                        flg = True
                if(hgt_ms=='in'):
                    if(hgt>=59 and hgt <=79):
                        flg = True
                if(flg):
                    flg = False
                    hcl = ele['hcl']
                    if(len(hcl)==7):
                        if(hcl[0]=="#"):
                            if re.match('^[a-f0-9]+$',hcl[1:]):
                                flg = True
                    if(flg):
                        ecl = ele['ecl']
                        if(ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                            pid = ele['pid']
                            if(len(pid)==9):
                                if re.match('^[0-9]+$',pid):
                                    vld = True
    return vld
 def count_valid(lst):    
    valid = 0
    for ele in lst:
        if(len(ele.keys())==8):
            if(valid_pass(ele)):
                valid = valid + 1
        elif(len(ele.keys())==7):
            if('cid' not in ele.keys()):
                if(valid_pass(ele)):
                    valid = valid + 1
    return valid
count_valid(lst)
