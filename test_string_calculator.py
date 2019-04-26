from string_calculator import *

def test_return_0_for_empty_string():
	assert add("") == 0

def test_single_numbers():
	assert add("1") == 1
	assert add("22") == 22

def test_add_stringNumbers():
	assert add("1,2") == 3
	assert add("3,5") == 8

def test_new_lines():
	assert add("1\n2") == 3

def test_different_delimiters():
	assert add("//;\n1;2") == 3
	assert add("//+\n1+10") == 11
	assert add("//abc\n1abc2abc3") == 6

def test_delimiters_mixed():
	assert add("//;\n1,2;3\n4") == 10

def test_minuses():
	assert add("//=\n1-2") == 3

def test_reject_negetive_numbers():
	assert raises(ValueError, add("-1"))
	assert raises(ValueError, add("1,-2"))
