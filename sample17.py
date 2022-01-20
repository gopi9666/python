n=int(input("please enter a number"))
for i in range(1,n+1):
    if (n%i==0):
        print("factors of given number i are:::")
        print(i)
        i+=i