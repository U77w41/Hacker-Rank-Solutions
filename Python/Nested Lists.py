if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ele= [name,score]
        records.append(ele)
        
#################################
mrks = []
for i in range(len(records)):
    a = records[i][1]
    mrks.append(a)

mn = min(mrks)
nw_mrks= []
for x in mrks:
    if x != mn:
        nw_mrks.append(x)
        
mini = min(nw_mrks)       
  


results = []
for i in range(len(records)):
    if records[i][1] == mini:
        b = records[i][0]
        results.append(b)
        
for names in sorted(results):
    print(names)

