class Multifunctions():
    def subfields():
        print("Sub-fields in AI:")
        subfields=['Machine Learning','Neural Networks', 'Vision','Robotics','Speech Processing','Natural Language Processing']
        for field in subfields:
            print(field)

    def OddEven():
        num=int(input("Enter the number:"))
        if((num%2)==1):
            print(num,"is Odd number")
        else:
            print(num,"is Even number")

    def MarriageEligibility():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
    
        if Gender=="Male":
            if Age>=21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            if Age>=18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")   

    def markpercentage():
        num1=int(input("Subject1="))
        num2=int(input("Subject2="))
        num3=int(input("Subject3="))
        num4=int(input("Subject4="))
        num5=int(input("Subject5="))
        
        add=num1+num2+num3+num4+num5
        percent=(add/500)*100
        
        print("Total:",add)
        print("Percentage:",percent)

    def triangle():
        num1=int(input("Height:"))
        num2=int(input("Breadth:"))
        Area=(num1*num2)/2
        print("Area of Triangle:(Height*Breadth)/2")
        print("Area of Triangle:",Area)
    
        num1=int(input("Height1:"))
        num2=int(input("Height2:"))
        num3=int(input("Breadth:"))
        Perimeter=num1+num2+num3
        print("Perimeter formula:Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Perimeter)