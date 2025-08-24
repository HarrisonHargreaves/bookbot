def count_words(text):
	words = text.split()
	return len(words)

def count_each_character(text):
	text = text.lower()
	character_count = {}
	for char in text:
		if char.isalpha():  # Consider only alphanumeric characters
			character_count[char] = character_count.get(char, 0) + 1
	return character_count

def sort_character_count(character_count):
	return dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))