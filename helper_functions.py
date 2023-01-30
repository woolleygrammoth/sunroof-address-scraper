def get_numeric(string: str) -> int: 
    '''
    Extracts only the numeric characters in a string and returns its integer version
    '''
    number = string.split(' ')[0]
    return int(number.replace(',', ''))

