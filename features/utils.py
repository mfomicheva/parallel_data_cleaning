

def zero_safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0.
