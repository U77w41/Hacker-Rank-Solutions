if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    


st = set()

for a in arr:
    st.add(a)

mx = max(st)
st.remove(mx)
print(max(st))





# mylist=list(arr)
# maxScore=max(mylist)

# if(maxScore != n):
#     mylist = filter(lambda x : x!=maxScore , mylist)
# print(max(mylist))
