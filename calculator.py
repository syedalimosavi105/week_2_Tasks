def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return None  # cannot divide by zero
    else:
        return None  # invalid operator

# Sample calls
print(calc(5, 3, "+"))  # 8
print(calc(5, 3, "-"))  # 2
print(calc(5, 3, "*"))  # 15
print(calc(5, 0, "/"))  # None (division by zero)
print(calc(5, 3, "%"))  # None (invalid op)