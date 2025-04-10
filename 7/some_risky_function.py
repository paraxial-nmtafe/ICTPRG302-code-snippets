def risky(value):
    if type(value) == str:
        return -1
    elif type(value) == int:
        result = 643 % value
        if result > 5:
            return 256
        else:
            return result
    else:
        return 7