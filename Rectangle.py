class Rectangle:
    def CalculateArea(self):
        print("Enter width")
        self.s=float(input())
        print("Enter height")
        self.h=float(input())
        area=self.s*self.h
        print("Area of rectangle is %f"%(area))
    def CalculatePerimeter(self):
         perimeter=(2*self.s)+(2*self.h)
         print("Perimeter of rectangle is %f"%(perimeter))
c=Rectangle()
c.CalculateArea()
c.CalculatePerimeter()
