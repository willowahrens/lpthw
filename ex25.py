def break_words(stuff):
	"""this function will break words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
 	"""sorts the words."""
 	return sorted(words)

def print_first_word(words):
 	"""prints the first word after popping it off."""
 	word = words.pop(0)
 	print word

def print_last_word(words):
 	"""prints the last word after popping it off."""
 	word = words.pop(-1)
 	print word

def sort_sentence(sentence):
 	"""takes in a full sentence and returns the sorted words."""
 	words = break_words(sentence)
 	return sort_words(words)

def print_first_and_last(sentence):
 	""" prints the first and last words of the sentence."""
 	words = break_words(sentence)
 	print_first_word(words)
 	print_last_word(words)

def print_first_and_last_sorted(sentence):
 	"""sorts the words then prints the first and last one."""
 	words = sort_sentence(sentence)
 	print_first_word(words)
 	print_last_word(words) 



 	

#  	lpthw(master)[ 2 ] > python
# Python 2.7.10 (default, Jul 30 2016, 19:40:32)
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25
# >>> sentence = "all good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['all', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['all', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# all
# >>> ex25.print_last_word(words)
# wait.
# >>> wrods
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'wrods' is not defined
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# all
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['all', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# all
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# all
# who