
def add(stringDigits):
	stringDigits = normalise_delim(stringDigits)
	if stringDigits:
		return add_string_numbers(stringDigits)
	else:
		return 0

def normalise_delim(stringDigits):
	stringDigits = normalise_diff_delim(stringDigits)
	stringDigits = stringDigits.replace("\n", ",")
	return stringDigits

def normalise_diff_delim(stringDigits):
	if stringDigits.startswith("//"):
		delim_spec, stringDigits = stringDigits.split("\n", 1)
		delimt = delim_spec[2:]
		stringDigits = stringDigits.replace(delimt, ",")
	return stringDigits

def add_string_numbers(stringDigits):
	numbers = map(int, stringDigits.split(","))
	check_numbers(numbers)
	return sum(numbers)

def check_numbers(numbers):
	if any(number < 0 for number in numbers):
		raise ValueError
