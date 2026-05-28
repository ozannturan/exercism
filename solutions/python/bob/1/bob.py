def response(hey_bob):
    clear = hey_bob.strip()
    
    if not clear:
        return "Fine. Be that way!"
    
    question = clear.endswith("?")
    shout = clear.isupper()
    
    if shout and question:
        return "Calm down, I know what I'm doing!"
    elif shout:
        return "Whoa, chill out!"
    elif question:
        return "Sure."
    else:
        return "Whatever."
