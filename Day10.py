lst = [0,115,134,121,184,78,84,77,159,133,90,71,185,152,165,39,64,85,50,20,75,2,120,137,164,101,56,153,63,70,10,72,37,86,27,166,186,154,131,1,122,95,14,119,3,99,172,111,142,26,82,8,31,53,28,139,110,138,175,108,145,58,76,7,23,83,49,132,57,40,48,102,11,105,146,149,66,38,155,109,128,181,43,44,94,4,169,89,96,60,69,9,163,116,45,59,15,178,34,114,17,16,79,91,100,162,125,156,65]
lst.sort()

def adap(lst):    
    jolt_ada = {1:0, 3:0}
    initial_jolt = 0
    for i in range(len(lst)):
        if(abs(initial_jolt - lst[i])==3):
            jolt_ada[3] = jolt_ada[3] + 1
        elif(abs(initial_jolt - lst[i])==1):
            jolt_ada[1] = jolt_ada[1] + 1
        initial_jolt = lst[i]
    return jolt_ada[1]*(jolt_ada[3]+1)
adap(lst)

def adapt_all(lst):    
    res_dct = {}

    res_dct[0] = 1

    for ele in lst[1:]:
        for j in range(1,4,1):
            if(ele - j in res_dct):
                if(ele in res_dct):
                    res_dct[ele] = res_dct[ele] + res_dct[ele - j]
                else:
                    res_dct[ele] = res_dct[ele - j]
    return res_dct[lst[-1]]
adapt_all(lst)
