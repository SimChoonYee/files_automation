#https://www.python-course.eu/python3_multiple_inheritance.php
#https://realpython.com/python-super/

#super: extends functionality of inherited method
#What is the meaning of class something(object)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)
    
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
    ##1
    #def __init__(self, length):
        #self.length = length
        
    #def area(self):
        #return self.length * self.length
    
    #def perimeter(self):
        #return 4*self.length
        
class Cube(Square):
    ##Use super() to exnted the area calculation
    ##you can skip defining it, and the .__init__() of the superclass (Square) will be called automatically
    
    def surface_area(self):
        ##Caution: Note that in our example above, super() alone won’t make the method calls for you: 
        ##you have to call the method on the proxy object itself.
        face_area =  super().area() 
        return 6 * face_area
    
    def volume(self):
        face_area = super().area()
        return face_area * self.length
        
    
if __name__=="__main__":
    square = Square(4)
    print(square.area())
    
    rectangle = Rectangle(2,4)
    print(rectangle.area())
    
    cube = Cube(3)
    print(cube.surface_area())
    print(cube.volume())