for n in range(0,151,1):
    print(n)


for n in range(5,1000,5):
    print(n)


#you need an elif if you want to print the word and not the number
#you need an else if you want to print the numbers 
for n in range(1,101,1):
    if n % 10 == 0:
        print("coding")
    elif n % 5 == 0:
        print("coding dojo")
    else:
        print (n)


#you need to create a variable  to store the number 
sum = 0
for n in range(500001):
    if n % 2 != 0: 
        sum += n
        print(sum)


for n in range(2018,0,-4):
    print(n)



#you con place variables inside of a loop
low_num = 1
high_num = 10
mult = 3
for n in range(low_num,high_num,+ 1):
    if n % mult == 0:
        print(n)