n=int(input("please enter a number"))
count=0,
for i in range(1,n+1):
    if (n%i==0):
        print(i)
        count+=1
print("number of factors of given number is:",count)        
        