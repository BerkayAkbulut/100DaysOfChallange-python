def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


# add(1, 2, 3, 4, 5)


def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs.get("add")
    print(n)
    n *= kwargs["multiply"]
    print(n)
    n = kwargs.get("7")
    print(n)


calculate(2, add=3, multiply=5)
