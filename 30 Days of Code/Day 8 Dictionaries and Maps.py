# Enter your code here. Read input from STDIN. Print output to STDOUT

number  = input()
phone_book = {}
name= None
phone = None
start = 0
while start < int(number):
    name, phone = map(str, input().split())
    phone_book[name.lower()] = phone
    start = start+1

for x in range(int(number)):
    try:
        name = input()
        if name in phone_book.keys():
            print(name+f"={phone_book[name]}")
        else:
            print('Not found')
    except EOFError:
        break