#
# def str_len(str_in: str) -> str:
#     """
#     Given a string parameter, this function should return the length of the parameter.
#     """
#
#     return len(str_in)
#
# def first_char(str_in: str) -> str:
#     """
#     Given a string parameter, this function should return the first letter of the parameter.
#     """
#
#     return str_in[0]
#
#
# def last_char(str_in: str) -> str:
#     """
#     Given a string parameter, this function should return the last letter of the parameter..
#     """
#
#     return str_in[-1]

def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    # for i in len(str_in[i]):
    #     if sub_str_in == str_in[int(i)][int(len(sub_str_in))]:
    #         return True
    #     else:
    #         return False

    str_in.index(sub_str_in)




    # if sub_str_in == str_in[i][len(str_in)-len(sub_str_in)]:
    #     return True
    # elif sub_str_in != str_in[0][len(str_in)-len(sub_str_in)]:
    #     return False
#
# def substring(str_in: str, start: int, stop: int) -> str:
#     """
#     Returns the substring of a string.
#
#     Keyword arguments:
#     str_in -- the string in which to generate a substring from
#     start -- starting position of the input parameter to start the substring (inclusive)
#     stop -- stopping position of the input parameter to stop the substring (exclusive)
#     """
#
#     sub_str = str_in[start:stop]
#     return sub_str
#     # print(sub_str)
#
#
# def opposite_case(str_in: str) -> str:
#     """
#     Given a string parameter, this function returns the same string back with each letter having the opposite case.
#     Example:
#     When input = "Python" the function returns "pYTHON"
#     """
#
#     print(str_in.swapcase())


# opposite_case('Hey')

# substring('zipcode', 1, 4)


input_has_substring('amber', 'am')
