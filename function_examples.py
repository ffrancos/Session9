def greet  ():
    """
    simple function printing hello
    :return:
    """
    print("hello!")
    return 0

greet()
x=greet()
print(x)

def greet_improved(name):
    """

    :param name: the name of the person to greet
    :return: None
    """
    print("Hello",name)
greet_improved("John")
greet_improved("Jane")

def custom_op(x=0,y=0):
    """
    Custom op:10x+y
    :param x: first number
    :param y: second number
    :return: number, 10x+y
    """

    result = 10*x+y
    return result
print(custom_op(5,8))
x=custom_op(5,9)
print(f"theresult of custom op is:{x}")
x=custom_op(y=9,x=5)
print(f"the result of custom_op is:{x}")
def bond_intro(name):
    print("the name is:",name)

def bond_name(first,last):
    return f"{last},{first} {last}"

print(bond_name("felipe", "francos"))
bond_intro(bond_name("felipe", "francos"))