def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
        print("This is the end print statement after decorator.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")
    print("This is the decorated function.")


say_hello()