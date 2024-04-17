def add(x: float, y: float) -> float:
    return(float(x)+float(y))

def multiply(x: float, y: float) -> float:
    return(float(x)*float(y))

def square(x: float) -> float:
    return(multiply(x, x))

def add_squares(x: float, y: float) -> float:
    x = square(x)
    y = square(y)
    return(add(x,y))

def main():
    a=add(3,4)
    b=multiply(3,4)
    c=square(5)
    d=add_squares(3,4)
    print(a,b,c,d)

main()
