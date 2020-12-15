while(True):
  mod_arr = np.where((tgt_cp%arr)==0)[0]
  if(mod_arr.shape[0] > 0):
    idx, tgt_val = mod_arr, tgt_cp
    break
  tgt_cp = tgt_cp + 1
print(arr[idx]*(tgt_val-tgt))


arr = np.asarray([x for x in lst if x != 'x'])
idx_arr = np.asarray([lst.index(x) for x in arr])
idx_dct = {}
for i in range(len(arr)):
    idx_dct[arr[i]] = idx_arr[i]
since = time.time()
strn = ""

for k,v in idx_dct.items():
    strn = strn+"(t+%s)mod%s,"%(v,k)
print("https://www.wolframalpha.com/input/?i=%s"%(strn.replace('+')))
