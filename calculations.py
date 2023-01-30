def calculation(operator_, second_number, first_number):
    if operator_ == 'add':
        return first_number + second_number
    elif operator_ == 'subtract':
        return  first_number - second_number
    elif operator_ == 'multiply':
        return first_number * second_number
    else:
        return int(first_number / second_number)


print(calculation(operator_=input(), first_number=int(input()), second_number=int(input())))
