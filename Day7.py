f = open('input.txt')

dct = {}
dct_cnt = {}
for line in f:
    if line != '\n':
        a, b = line.split(' contain ')
        b = b.strip('.\n')
        a = a.replace('bags','').replace('bag','').rstrip(' ')
        tmp_lst = b.split(', ')
        for ele in tmp_lst:
            if(a in dct):
                dct[a].append(re.sub(r'[0-9]+', '', ele).replace('bags','').replace('bag','').lstrip(' ').rstrip(' '))
                dct_cnt[a].append(re.sub(r'[a-z]+', '', ele).replace(' ',''))
            else:
                dct[a] = [re.sub(r'[0-9]+', '', ele).replace('bags','').replace('bag','').lstrip(' ').rstrip(' ')]
                dct_cnt[a] = [re.sub(r'[a-z]+', '', ele).replace(' ','')]
f.close()

def cnt_1(dct):
    cnt  = 0
    lst = []

    for k,v in dct.items():
        if('shiny gold' in v):
            cnt = cnt + 1
            lst.append(k)

    tmp_lst = lst.copy()
    while(len(tmp_lst)>0):
        sr_ele = tmp_lst.pop(0)
        for k,v in dct.items():
            if(sr_ele in v):
                if(k not in lst):
                    lst.append(k)
                    tmp_lst.append(k)
                    cnt = cnt + 1
    return cnt
def cnt_2(shiny_bags, shiny_bags_cnt):
    cnt = 1
    for i in range(len(shiny_bags)):
        if(shiny_bags[i]=='no other'):
            return 1
        else:
            cnt = cnt + int(shiny_bags_cnt[i])*cnt_2(dct[shiny_bags[i]], dct_cnt[shiny_bags[i]])
    return cnt

shiny_bags = dct['shiny gold']
shiny_bags_cnt = dct_cnt['shiny gold']
cnt_1(dct), cnt_2(shiny_bags, shiny_bags_cnt)
