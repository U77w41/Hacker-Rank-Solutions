
def merge_the_tools(string, k):
    # your code goes here
    
    substring=[]
    
    for i,l in enumerate(string):
        if l not in substring:
            substring.append(l)
        if i%k==k-1:
            print(''.join(substring))
            substring=[]

            
            
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)