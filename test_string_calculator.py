from string_calculator import *

def test_return_0_for_empty_string():
	result = add("") 
	assert result == 0

def test_single_digit_strings():
	result = add("1")
	assert result == 1

	result = add("22")
	assert result == 22

def test_string_with_two_or_more_elements_return_sum():
	result = add("1, 2")
	assert result == 3

	result = add("2, 3")
	assert result == 5

	result = add("1,2,3,4")
	assert result == 10

def test_newline_delimiter():
	result = add("1\n2,3")
	assert result == 6

def test_different_delimiters():
	result = add("//;\n1;2")
	assert result == 3

def test_negative_numbers_raises_exception():
	result = add("-1")
	assert NegativeError