list=[23,45,56,23,90,77]
num=int(input("please enter a number"))
count=0
for i in list:
    if num==i:
        count=count+1
if count!=0:
    print(count)
else:
    print("element not found")
    
    
 