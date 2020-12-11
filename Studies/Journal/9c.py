class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area of Rectangle:",(a*b))
        elif a!=None:
            print("Area of square:",(a*a))
        else:
            print("Nothing to find")
obj1=Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)