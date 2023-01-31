def get_numeric(string: str) -> int: 
    '''
    Extracts only the numeric characters in a string and returns its integer version
    '''
    number = string.split(' ')[0]
    if ',' in number: 
        number = number.replace(',', '')
    if '$' in number: 
        number = number.replace('$', '')
    if '.' in number: 
        return float(number)
    try: 
        return int(number)
    except ValueError: 
        return string
 