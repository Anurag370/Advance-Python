def greet(fx):

    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using our services.")

    return mfx


@greet
def hello():
    print("Hello World")


hello()