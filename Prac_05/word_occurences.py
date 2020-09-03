word_to_count = {}
text_input = input("Enter a string: ")
words = text_input.split()

for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1

words = list(word_to_count.keys())
words.sort()

longest_word = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, longest_word, word_to_count[word]))
