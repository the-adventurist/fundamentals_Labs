def grade_in_words(current_grade):
    if 2 <= current_grade <= 2.99:
        return 'Fail'
    elif current_grade <= 3.49:
        return 'Poor'
    elif current_grade <= 4.49:
        return 'Good'
    elif current_grade <= 5.49:
        return 'Very Good'
    elif current_grade <= 6.00:
        return 'Excellent'


print(grade_in_words(float(input())))
