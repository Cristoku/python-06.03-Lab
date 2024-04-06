import math

def circle_a(a):
    area=math.pi * (a**2)
    return area
                   
def triangle_a(a,b):
    area=(a*b)/2
    return area

def square_a(a):
    area=a**2
    return area

def get_float(argument):
    while True:
        value = float(input(argument))
        if value > 0:
            return value
        else:
            print("Wrong Input")
            
shapes= ["circle","triangle","square","rectangle"]

while True:
    
    shape = input("Enter name of the shape (circle | triangle | square) or stop:")
    if shape.lower() == "circle":
        a = get_float("Enter the length of the radius of the circle") 
        print(circle_a(a))    
                          
    elif shape.lower() == "triangle":
        a = get_float("Enter the legth of the base of the triangle") 
        b = get_float("Enter the length of the height")
        print(triangle_a(a,b))    
        
    elif shape.lower() == "square":
        a = get_float("Enter the length of the side of the square ")
        print(square_a(a))    
          
    elif shape.lower() == "stop":
        break

