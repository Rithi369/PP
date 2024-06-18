def rect(L,B):
    return(L*B)

def square(s):
    return(s*s)

def circle(r):
    return(3.14*r*r)

def triangle(b,h):
    return(0.5*b*h)

def main():
    L = int(input("Enter the length of the Rectangle :"))
    B = int(input("Enter the Breadth of the Rectangle :"))
    s = int(input("Enter the side of the square :"))
    r = int(input("Enter the radius of the circle :"))
    b = int(input("Enter base of the triangle :"))
    h = int(input("Enter the height of the triangle :"))

    print(f"Area of the Rectangle : {rect (L,B)}")
    print(f"Area of the Square : {square(s)}")
    print(f"Area of the Circle : {circle(r)}")
    print(f"Area of the Triangle : {triangle(b,h)}")

if __name__=="__main__":
    main()




