# Function One: Takes a number as input and returns its square.
def function_one(number):
    """
    This function takes a number as input and returns its square.

    Parameters:
    - number (int or float): The input number.

    Returns:
    - int or float: The square of the input number.
    """
    return number ** 2


# Function Two: Takes a string and returns its uppercase version.
def function_two(input_string):
    """
    This function takes a string as input and returns its uppercase version.

    Parameters:
    - input_string (str): The input string.

    Returns:
    - str: Uppercase version of the input string.
    """
    return input_string.upper()


# Function Three: Combines the results of function_one and function_two.
def function_three(input_number, input_string):
    """
    This function combines the results of function_one and function_two.

    Parameters:
    - input_number (int or float): The input number for function_one.
    - input_string (str): The input string for function_two.

    Returns:
    - tuple: A tuple containing the square of input_number and the uppercase version of input_string.
    """
    result_one = function_one(input_number)
    result_two = function_two(input_string)
    return result_one, result_two


# Test Cases for Function Three
if __name__ == "__main__":
    # Test Case 1
    test_result_1 = function_three(5, "hello")
    print("Test Case 1:", test_result_1)

    # Test Case 2
    test_result_2 = function_three(2.5, "world")
    print("Test Case 2:", test_result_2)

    # Test Case 3
    test_result_3 = function_three(0, "python")
    print("Test Case 3:", test_result_3)

    # Test Case 4
    test_result_4 = function_three(-3, "prep")
    print("Test Case 4:", test_result_4)
