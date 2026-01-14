''' Write a Python program to access a function inside a function. '''

def outer_func(text):
    def inner_func():
        print(f"{text}")

    return inner_func

func = outer_func("Hello World")
func()