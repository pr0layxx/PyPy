def sum_all(*args):
    print(args)
    for i in args:
        print(i**3)
    return sum(args)


print(sum_all(1, 3, 4))


# kwargs
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="prolay", lastName="Das")
print_kwargs(Name= "prolay", friend= "Nandita", lastName="Das")