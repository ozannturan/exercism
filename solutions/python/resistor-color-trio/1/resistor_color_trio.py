def label(colors):
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
    
    main_value = (col[colors[0]] * 10) + col[colors[1]]
    zero_count = col[colors[2]]
    total = main_value * (10 ** zero_count)
    
    if total >= 1000000000:
        value = total / 1000000000
        unit = "gigaohms"
    elif total >= 1000000:
        value = total / 1000000
        unit = "megaohms"
    elif total >= 1000:
        value = total / 1000
        unit = "kiloohms"
    else:
        value = total
        unit = "ohms"
    
    if value.is_integer():
        return f"{int(value)} {unit}"
    else:
        return f"{value} {unit}"