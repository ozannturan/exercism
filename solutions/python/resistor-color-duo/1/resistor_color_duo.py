def value(colors):
    col = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    
    first_value = col[colors[0]]
    second_value = col[colors[1]]
    result = (first_value * 10) + second_value
    return result
