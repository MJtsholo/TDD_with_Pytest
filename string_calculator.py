import re

class NegativeError(Exception):
	pass

def convert(value):
	if value < 0:
		raise NegativeError

def add(stringDigits):
	if stringDigits == "":
		return 0
	try:
		return int(stringDigits)
	except ValueError:
		try:
			m = re.split("//(.)\n(.*)", stringDigits)
			delimiter = m[1]
			stringDigits = m[2]
		except:
			delimiter = "\n,"
		number_split = [int(n) for n in re.split("[%s]*" % delimiter, stringDigits)]
		return sum(number_split)
