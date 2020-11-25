from os import system 
system("color 06")
x = 1
y = 1
op = "1"

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def div(x, y):
    return x / y
def mult(x, y):
    return x * y

def calc(x, y, op):
    while True:
        print("                     ")
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        op = input("1/2/3/4: ")

        if op in ("1", "2", "3", "4"):

            x = input("First Int: ")
            y = input("Second Int: ")

            try:
                x = float(x)
                y = float(y)

                if op == "1":
                    print(x, "+", y, "=", add(x, y))
                elif op == "2":
                    print(x, "-", y, "=", sub(x, y))
                elif op == "3":
                    print(x, "*", y, "=", mult(x, y))
                elif op == "4":
                    print(x, "/", y, "=", div(x, y))
                else:
                    print("stupid idiot put invalid wrong dumbstupid")

            except ValueError:
                    print("wrong input idiot")


while True:
    calc(x, y, op)
