f = open("input.txt")
lst = []
for line in f:
    lst.append(line.strip('\n'))
f.close()
len(lst)


drn_dic = {'E': {'R90':'S','R180':'W','R270':'N','L90':'N','L180':'W','L270':'S'},
'W' : {'R90':'N','R180':'E','R270':'S','L90':'S','L180':'E','L270':'N'},
'N' : {'R90':'E','R180':'S','R270':'W','L90':'W','L180':'S','L270':'E'},
'S' : {'R90':'W','R180':'N','R270':'E','L90':'E','L180':'N','L270':'W'}}

dct = {'E':0,'N':0,'S':0,'W':0}
curr_dir = 'E'
for ele in lst:
    if(ele[0] == 'F'):
        dct[curr_dir] = dct[curr_dir] + int(ele[1:])
    elif(ele[0] in ['N','S','W','E']):
        dct[ele[0]] = dct[ele[0]] + int(ele[1:])
    elif(ele[0] in ['L','R']):
        curr_dir = drn_dic[curr_dir][ele]
print(abs(dct['E']-dct['W'])+abs(dct['N']-dct['S']))

curr_dir = ['E','N']
wp_units = {'E':10,'N':1}
dct = {'E':0,'N':0}
for ele in lst:
    if(ele[0]=='F'):
        frd1, frd2 = wp_units[curr_dir[0]]*int(ele[1:]), wp_units[curr_dir[1]]*int(ele[1:])
        dct[curr_dir[0]] = dct[curr_dir[0]] + frd1
        dct[curr_dir[1]] = dct[curr_dir[1]] + frd2
    elif(ele[0] in ['N','S','W','E']):
        if(ele[0] == 'N'):
            wp_units['N'] = wp_units['N'] + int(ele[1:])
        elif(ele[0] == 'S'):
            wp_units['N'] = wp_units['N'] - int(ele[1:])
        elif(ele[0] == 'E'):
            wp_units['E'] = wp_units['E'] + int(ele[1:])
        elif(ele[0] == 'W'):
            wp_units['E'] = wp_units['E'] - int(ele[1:])
    elif(ele[0] in ['L','R']):
        if(ele[0] == 'L'):
            itr = int(int(ele[1:])/90)
            for i in range(itr):
                wp_units['E'], wp_units['N'] = -1*wp_units['N'], wp_units['E']
        if(ele[0] == 'R'):
            itr = int(int(ele[1:])/90)
            for i in range(itr):
                wp_units['E'], wp_units['N'] = wp_units['N'], -1*wp_units['E']
print(abs(dct['E'])+abs(dct['N']))
print(dct)
