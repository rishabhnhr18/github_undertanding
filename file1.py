def dec_func(func):
    def wrapper():
        print("1st")
        func()
        print("2nd")
    return wrapper

@dec_func
def greet():
    print("Good Morning, Guys")
    
greet()