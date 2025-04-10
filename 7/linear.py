"""
A simple module for getting the y value for any linear function.
"""

def linear_result(slope, iteration, constant):
    """
        Arguments:
        - slope: Any number representing the slope of the line
        - iteration: Any number, representing the 'X' value of the equation
        - constant: Any number: a constant offset of the line.

        Returns:
        - A number, being the Y coordinate of the line at the time of 'iteration'
    """
    return slope * iteration + constant

