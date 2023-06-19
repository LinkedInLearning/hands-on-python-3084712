name = input("What's your name?")
template1 = f"hello, world 1 {name}"
template2 = "hello, world 2 {}"
print(template1)

print(template2.format(name))
