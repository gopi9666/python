pmarks=float(input("please enter project marke"))
internal=float(input("please enter internal marke"))
external=float(input("please enter external marke"))
if (pmarks>=50)&(internal>=50)&(external>=50):
    
  total_marks=(70/100*pmarks)+(20/100*external)+(10/100*internal)
    
elif total_marks>=90:
    print("total marks are:::",total_marks)
    print("you got A grade"
        
elif  total_marks>=75:
    print("total marks are:::",total_marks)
    print("you got B grade"
elif  total_marks>=50:
    print("total marks are:::",total_marks)
    print("you got C grade"
                
            
                
else:
    print("your project marks are:::",pmarks)
    print("you faild")
else:
    print("your internal marks are:::",internal)
    print("you faild")
        else:
            print("your external marks are:::",external)
            print("you faild")