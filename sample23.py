count1=10
count2=90
for i in range(5):
    for j in range(5):
        if i%2==0:
            print(count1,end=" ")
            count1=count1+1
    
        
        else:
            print(count2,end=" ")
            count2=count2-1
    print()        