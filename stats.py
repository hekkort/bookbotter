import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()
	
def count_words(path_to_file):
	str = get_book_text(path_to_file)
	str_lst = str.split()
	return len(str_lst)

def count_chars(path_to_file):
    lower_book = get_book_text(path_to_file).lower()
    char_dict = {}
    for char in lower_book:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def sorted(d):
    lst = []
    for item in d:
        if item.isalpha():
            lst.append({"char": item, "num": d[item]})

    lst.sort(reverse=True, key=sort_on)
    return lst

def report(d):
    s = sorted(d)
    full_string = f"""============ BOOKBOT ============\n
    Analyzing book found at {sys.argv[1]}...\n
    ----------- Word Count ----------\n
    Found {count_words(sys.argv[1])} total words\n
    --------- Character Count -------\n"""
    for item in s:
        full_string = full_string + (f"{item['char']}: {item['num']}\n")
    print(full_string + "============= END ===============")
    #mid = begin_string + lst

    #end_string = "============= END ==============="

    #final = mid + end_string

    #print(final)