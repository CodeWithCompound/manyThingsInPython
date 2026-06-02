import sys

def add(a, b):
    c = a + b
    return c

def convert(x, y):
    def to_num(v):
        if isinstance(v, (int, float)):
            return v                   
        try:
            return int(v)
        except (ValueError, TypeError):
            return float(v)

    try:
        a = to_num(x)
        b = to_num(y)
        return add(a, b)
    except (ValueError, TypeError):
        print("Conversion Fail, please enter a valid number")
        sys.exit(404)


print(convert(4, "65.0"))
print(convert("10", "20"))
print(convert(3.5, "2"))
print(convert(4.0, 5))
print(convert("hello", "world"))