def absolute_values(sequence):
    result = [abs(float(x)) for x in sequence.split()]
    return result


print(absolute_values(input()))
