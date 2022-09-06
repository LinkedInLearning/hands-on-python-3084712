

RUN_INDENTED = False

message = "running unindented"

if RUN_INDENTED:
    message = "running indented"

print(message)


def my_function():
    greet = "Hello"
    return greet


if __name__ == "__main__":
    print(my_function())
