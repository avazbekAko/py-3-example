from time import sleep

def my_func(add):
    for a in range (1, 5):
        sleep(1)
        print(add, a)

my_func("hello")
my_func("world")
