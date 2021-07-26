def hi():
    while True:
        try:
            a=int(input("enter the denominator of Pi radian\n"
            "(choose from 1,2,3,4,6)\n"
            "Enter here:"))
            if a<=0 or a>=7 or a==5:
                print("Enter the given digits")
                #hi()                       
            else:
                return a                         
        except Exception:
            print("enter a valid type")                  
ant=hi()
print(ant)
