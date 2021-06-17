"""
Python Class


If white sheet is visible, the uncovered area of white sheet should be greater than zero.
Visible_Area = Red_Area + Green_Area - Violet_Area
Red_Area = intersection(BlackSheet, WhiteSheet)
Green_Area = intersection(BlackSheet2, WhiteSheet)
Violet_Area = intersection(Red, Green)
	= intersection(BlackSheet1, BlackSheet2, WhiteSheet)
Eventually, we have the following:
Visible_Area = intersection(BlackSheet1, WhiteSheet) + intersection(BlackSheet2, WhiteSheet) - intersection(BLackSheet1, BlackSheet2, WhiteSheet)
"""
    