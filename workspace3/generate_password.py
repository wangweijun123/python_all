# Use an import statement at the top
import random
word_file = 'E:/study/udacity/python/workspace3/words.txt'
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    print("word_list:", word_list)
    size = len(word_list)
    print("size:", size)
    selected_words = random.sample(word_list, 3)
    print("selected_words:", selected_words)
    result = ""
    for item in selected_words:
        result += item
    return result


def generate_password2():
    return ''.join(random.sample(word_list,3))


# test your function
print(generate_password())

print(generate_password2())