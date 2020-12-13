import copy
f = open('input.txt')
lst = []
for line in f:
    tmp = list(line.strip('\n'))
    lst.append(tmp)
f.close()
print(len(lst))

def rule1(lst,i,j):
    a,b,c,d,e,f,g,h = (i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i+1,j+1),(i-1, j+1), (i+1, j-1)
    visited = 0
    cnt = 0
    flg = False
    if(i-1 >= 0):
        visited = visited + 1
        if(lst[a[0]][a[1]] == 'L' or lst[a[0]][a[1]] == '.'):
            cnt = cnt + 1
    if(i+1 < len(lst)):
        visited = visited + 1
        if(lst[b[0]][b[1]] == 'L' or lst[b[0]][b[1]] == '.'):
            cnt = cnt + 1
    if(j-1 >= 0):
        visited = visited + 1
        if(lst[c[0]][c[1]]=='L' or lst[c[0]][c[1]]=='.'):
            cnt = cnt + 1
    if(j+1 < len(lst[0])):
        visited = visited + 1
        if(lst[d[0]][d[1]]=='L' or lst[d[0]][d[1]]=='.'):
            cnt = cnt + 1
    if(i-1 >= 0 and j-1>=0):
        visited = visited + 1
        if(lst[e[0]][e[1]] == 'L' or lst[e[0]][e[1]] == '.'):
            cnt = cnt + 1
    if(i+1 < len(lst) and j+1 < len(lst[0])):
        visited = visited + 1
        if(lst[f[0]][f[1]] == 'L' or lst[f[0]][f[1]] == '.'):
            cnt = cnt + 1
    if(i-1 >= 0 and j+1 < len(lst[0])):
        visited = visited + 1
        if(lst[g[0]][g[1]]=='L' or lst[g[0]][g[1]]=='.'):
            cnt = cnt + 1
    if(i+1 < len(lst) and j-1>=0):
        visited = visited + 1
        if(lst[h[0]][h[1]]=='L' or lst[h[0]][h[1]]=='.'):
            cnt = cnt + 1
    if(cnt == visited):
        flg = True
    return flg

def rule2(lst,i,j):
    a,b,c,d,e,f,g,h = (i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i+1,j+1),(i-1, j+1), (i+1, j-1)
    cnt = 0
    flg = False
    if(i-1 >= 0):
        if(lst[a[0]][a[1]] == '#'):
            cnt = cnt + 1
    if(i+1 < len(lst)):
        if(lst[b[0]][b[1]] == '#'):
            cnt = cnt + 1
    if(j-1 >= 0):
        if(lst[c[0]][c[1]]=='#'):
            cnt = cnt + 1
    if(j+1 < len(lst[0])):
        if(lst[d[0]][d[1]]=='#'):
            cnt = cnt + 1
    if(i-1 >= 0 and j-1>=0):
        if(lst[e[0]][e[1]] == '#'):
            cnt = cnt + 1
    if(i+1 < len(lst) and j+1 < len(lst[0])):
        if(lst[f[0]][f[1]] == '#'):
            cnt = cnt + 1
    if(i-1 >= 0 and j+1 < len(lst[0])):
        if(lst[g[0]][g[1]]=='#'):
            cnt = cnt + 1
    if(i+1 < len(lst) and j-1>=0):
        if(lst[h[0]][h[1]]=='#'):
            cnt = cnt + 1
    if(cnt >= 4):
        flg = True
    return flg
def rule12(lst,i,j):
    a,b,c,d,e,f,g,h = [i-1,j],[i+1,j],[i,j-1],[i,j+1],[i-1,j-1],[i+1,j+1],[i-1, j+1], [i+1, j-1]
    s,t,u,v,w,x,y,z = [i-1,j],[i+1,j],[i,j-1],[i,j+1],[i-1,j-1],[i+1,j+1],[i-1, j+1], [i+1, j-1]
    cnt = 0
    flg_arr = {'a':False,'b':False,'c':False,'d':False,'e':False,'f':False,'g':False,'h':False}
    flg = False
    visited = 0
    while(a[0]>=0):
        flg_arr['a'] = True
        if(lst[a[0]][a[1]] == 'L'):
            cnt = cnt + 1
            break
        if(lst[a[0]][a[1]] == '#'):
            break
        if(lst[a[0]][a[1]] == '.'):
            if(a[0] == 0):
                cnt = cnt + 1
                break
        a[0] = a[0]-1
    a = s
    while(b[0] < len(lst)):
        flg_arr['b'] = True
        if(lst[b[0]][b[1]] == 'L'):
            cnt = cnt + 1
            break
        if(lst[b[0]][b[1]] == '#'):
            break
        if(lst[b[0]][b[1]] == '.'):
            if(b[0] == len(lst) - 1):
                cnt = cnt + 1
                break
        b[0] = b[0]+1
    b = t
    while(c[1] >= 0):
        flg_arr['c'] = True
        if(lst[c[0]][c[1]]=='L'):
            cnt = cnt + 1
            break
        if(lst[c[0]][c[1]] == "#"):
            break
        if(lst[c[0]][c[1]] == '.'):
            if(c[1] == 0):
                cnt = cnt + 1
                break
        c[1] = c[1]-1
    c = u
    while(d[1] < len(lst[0])):
        flg_arr['d'] = True
        if(lst[d[0]][d[1]]=='L'):
            cnt = cnt + 1
            break
        if(lst[d[0]][d[1]] == '#'):
            break
        if(lst[d[0]][d[1]] == '.'):
            if(d[1] == len(lst[0]) - 1):
                cnt = cnt + 1
                break
        d[1] = d[1] + 1
    d = v
    while(e[0]>= 0 and e[1]>=0):
        flg_arr['e'] = True
        if(lst[e[0]][e[1]] == 'L'):
            cnt = cnt + 1
            break
        if(lst[e[0]][e[1]] == '#'):
            break
        if(lst[e[0]][e[1]] == '.'):
            if(e[0] == 0 or e[1] == 0):
                cnt = cnt + 1
                break
        e[0] = e[0] -1
        e[1] = e[1] -1
    e = w
    while(f[0] < len(lst) and f[1] < len(lst[0])):
        flg_arr['f'] = True
        if(lst[f[0]][f[1]] == 'L'):
            cnt = cnt + 1
            break
        if(lst[f[0]][f[1]] == '#'):
            break
        if(lst[f[0]][f[1]] == '.'):
            if(f[0] == len(lst) - 1 or f[1] == len(lst[0]) -1):
                cnt = cnt + 1
                break
        f[0] = f[0] +1
        f[1] = f[1]+1
    f = x
    while(g[0] >= 0 and g[1] < len(lst[0])):
        flg_arr['g'] = True
        if(lst[g[0]][g[1]]=='L'):
            cnt = cnt + 1
            break
        if(lst[g[0]][g[1]] == '#'):
            break
        if(lst[g[0]][g[1]] == '.'):
            if(g[0] == 0 or g[1] == len(lst[0]) - 1):
                cnt = cnt + 1
                break
        g[0] = g[0]  - 1
        g[1] = g[1] + 1
    g = y
    while(h[0] < len(lst) and h[1]>=0):
        flg_arr['h'] = True
        if(lst[h[0]][h[1]]=='L'):
            cnt = cnt + 1
            break
        if(lst[h[0]][h[1]] == '#'):
            break
        if(lst[h[0]][h[1]] == '.'):
            if(h[0] == len(lst) - 1 or h[1] == 0):
                cnt = cnt + 1
                break
        h[0] = h[0] +1
        h[1] = h[1]-1
    h = z
    
    for ky, vl in flg_arr.items():
        if(vl):
            visited = visited + 1
    if(cnt == visited):
        flg = True
    #print(cnt, visited)
    return flg

def rule22(lst,i,j):
    a,b,c,d,e,f,g,h = [i-1,j],[i+1,j],[i,j-1],[i,j+1],[i-1,j-1],[i+1,j+1],[i-1, j+1], [i+1, j-1]
    s,t,u,v,w,x,y,z = [i-1,j],[i+1,j],[i,j-1],[i,j+1],[i-1,j-1],[i+1,j+1],[i-1, j+1], [i+1, j-1]
    cnt = 0
    flg_arr = {'a':False,'b':False,'c':False,'d':False,'e':False,'f':False,'g':False,'h':False}
    flg = False
    visited = 0
    while(a[0]>=0):
        flg_arr['a'] = True
        if(lst[a[0]][a[1]] == '#'):
            cnt = cnt + 1
            break
        if(lst[a[0]][a[1]] == 'L'):
            break
        a[0] = a[0]-1
    a = s
    while(b[0] < len(lst)):
        flg_arr['b'] = True
        if(lst[b[0]][b[1]] == '#'):
            cnt = cnt + 1
            break
        if(lst[b[0]][b[1]] == 'L'):
            break
        b[0] = b[0]+1
    b = t
    while(c[1] >= 0):
        flg_arr['c'] = True
        if(lst[c[0]][c[1]]=='#'):
            cnt = cnt + 1
            break
        if(lst[c[0]][c[1]] == "L"):
            break
        c[1] = c[1]-1
    c = u
    while(d[1] < len(lst[0])):
        flg_arr['d'] = True
        if(lst[d[0]][d[1]]=='#'):
            cnt = cnt + 1
            break
        if(lst[d[0]][d[1]] == 'L'):
            break
        d[1] = d[1] + 1
    d = v
    while(e[0]>= 0 and e[1]>=0):
        flg_arr['e'] = True
        if(lst[e[0]][e[1]] == '#'):
            cnt = cnt + 1
            break
        if(lst[e[0]][e[1]] == 'L'):
            break
        e[0] = e[0] -1
        e[1] = e[1] -1
    e = w
    while(f[0] < len(lst) and f[1] < len(lst[0])):
        flg_arr['f'] = True
        if(lst[f[0]][f[1]] == '#'):
            cnt = cnt + 1
            break
        if(lst[f[0]][f[1]] == 'L'):
            break
        f[0] = f[0] +1
        f[1] = f[1]+1
    f = x
    while(g[0] >= 0 and g[1] < len(lst[0])):
        flg_arr['g'] = True
        if(lst[g[0]][g[1]]=='#'):
            cnt = cnt + 1
            break
        if(lst[g[0]][g[1]] == 'L'):
            break
        g[0] = g[0]  - 1
        g[1] = g[1] + 1
    g = y
    while(h[0] < len(lst) and h[1]>=0):
        flg_arr['h'] = True
        if(lst[h[0]][h[1]]=='#'):
            cnt = cnt + 1
            break
        if(lst[h[0]][h[1]] == 'L'):
            break
        h[0] = h[0] +1
        h[1] = h[1]-1
    h = z
    
    if(cnt >= 5):
        flg = True

    return flg
def find_adjecent(lst):
    lst_cp = copy.deepcopy(lst)
    m = 0
    while(True):
        lst_cp1 = copy.deepcopy(lst_cp)
        for i in range(len(lst_cp1)):
            for j in range(len(lst_cp1[0])):
                if(lst_cp1[i][j] == 'L'):
                    flg = rule1(lst_cp, i, j)
                    if(flg):
                        lst_cp1[i][j] = '#'


        lst_cp2 = copy.deepcopy(lst_cp1)
        for i in range(len(lst_cp2)):
            for j in range(len(lst_cp2[0])):
                if(lst_cp2[i][j] == '#'):
                    flg = rule2(lst_cp1, i, j)
                    if(flg):
                        lst_cp2[i][j] = 'L'
        if(lst_cp2 == lst_cp1):
            break
        else:
            lst_cp = copy.deepcopy(lst_cp2)
            m = m+1
    cnt = 0
    for i in lst_cp1:
        for j in i:
            if j == '#':
                cnt = cnt+1
    return cnt
def find_occupied(lst):
    lst_cp = copy.deepcopy(lst)
    m = 0
    while(True):
        lst_cp1 = copy.deepcopy(lst_cp)
        for i in range(len(lst_cp1)):
            for j in range(len(lst_cp1[0])):
                if(lst_cp1[i][j] == 'L'):
                    flg = rule12(lst_cp, i, j)
                    if(flg):
                        lst_cp1[i][j] = '#'


        lst_cp2 = copy.deepcopy(lst_cp1)
        for i in range(len(lst_cp2)):
            for j in range(len(lst_cp2[0])):
                if(lst_cp2[i][j] == '#'):
                    flg = rule22(lst_cp1, i, j)
                    if(flg):
                        lst_cp2[i][j] = 'L'
        if(lst_cp2 == lst_cp1):
            break
        else:
            lst_cp = copy.deepcopy(lst_cp2)
            m = m+1
    cnt = 0
    for i in lst_cp1:
        for j in i:
            if j == '#':
                cnt = cnt+1
    return cnt
