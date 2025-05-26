from stats import count_words, count_chars, sorted, report
import sys

def main():

	#try:
	#	report(count_chars(sys.argv[1]))
	#except Exception:
	#	print("Usage: python3 main.py <path_to_book>")
	#	sys.exit(1)

	if len(sys.argv) == 2:
		report(count_chars(sys.argv[1]))

	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
main()
