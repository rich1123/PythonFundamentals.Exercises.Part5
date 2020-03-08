def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    reverse = value[::-1]
    if reverse == value:
        return True
    elif reverse != value:
        return False



# is_palindrome('madam')
