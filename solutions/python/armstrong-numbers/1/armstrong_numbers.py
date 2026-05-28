def is_armstrong_number(number):
    num_str = str(number)
    number_digits = len(num_str)
    sum = 0
    for num in num_str:
        sum += int(num) ** number_digits
    return sum == number
