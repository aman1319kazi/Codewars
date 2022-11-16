def even_or_odd(number):
    if bin(number)[-1] == '0':
        return "Even"
    else:
        return "Odd"