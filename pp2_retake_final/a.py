n = int(input())
gpa_cnt, gpa_occ = {}, {}          
                                  
while n > 0:
    x = input().split()
    gpa_occ[x[0]] = gpa_occ.get(x[0], 0) + 1     
    
    if x[0] not in gpa_cnt.keys():
        gpa_cnt[x[0]] = int(x[1])             
    else:                                    
        gpa_cnt[x[0]] += int(x[1])        

    n -= 1

gpa = {}        

for key, value in gpa_cnt.items():     
    gpa[key] = f'{value / gpa_occ[key]:.3f}'  


for key, value in sorted(gpa.items(), key=str):
    print(key + ': ' + value)

    # saled