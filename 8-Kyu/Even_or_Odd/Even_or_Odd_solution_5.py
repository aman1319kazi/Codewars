def even_or_odd(number):
    if number >= 0:
        step = 1
        end = number + 1
    else:
        step = -1
        end = number - 1

    iseven = False
    for x in range(0, end, step):
        if iseven:
            iseven = False
        else:
            iseven = True
    return "Even" if iseven else "Odd"