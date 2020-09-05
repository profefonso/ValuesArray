def getArray(items):
    return_array = []
    for value in items:
        if isinstance(value, list):
            return_array = return_array + getArray(value)
        else:
            return_array.append(value)

    return return_array