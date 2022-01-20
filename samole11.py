units=int(input("please enter number of units"))
if units<50:
    bill=units*0.75;
    print("no.of units are:::",units)
    print("the bill value is:::",bill)
elif units<=100:
    bill=units*2.10;
    print("no.of units are:::",units)
    print("the bill value is:::",bill)
elif units<=200:
    bill=units*2.50;
    print("no.of units are:::",units)
    print("the bill value is:::",bill)
elif units<=250:
    bill=units*2.80;
    print("no.of units are:::",units)
    print("the bill value is:::",bill)
else:
    bill=(50*0.75)+(100*2.10)+(100*2.50)+(units-250)*2.80
    print("the bill value is:::",bill)
    gst=(bill*10)/100
    bill=bill+gst
    print("the gst value is:::",gst)
    print("the Finallbill value is:::",bill)




