# Compare Strings

#run this program by typing python compare-strings.py on shell (with python installed)

def compare_strings(first_string,second_string):
	switch = False
	for char in first_string:
		if char in second_string:
			switch = True
			break
	return switch


def main():
	first = str(raw_input("Enter first String: "))
	second = str(raw_input("Enter Second String: "))
	if compare_strings(first,second):
		print "YES"
	else:
		print "NO"


if __name__ == "__main__":
	main()
