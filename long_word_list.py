def sentence_to_dict(sentence):
    word_dict = {}
    for word in sentence.split():
        word_dict[word] = len(word)
    return word_dict

def find_long_words(word_dict, length):
    long_words = []
    for word in word_dict:
        if word_dict[word] > length:
            long_words.append(word)
    return long_words


sentence = "This is a Python programming example for creating a dictionary"
word_dict = sentence_to_dict(sentence)
print("Word Dictionary:")
for word, length in word_dict.items():
    print(f"{word}: {length}")

user_length = int(input("\nEnter the length to search for words longer than: "))
long_words = find_long_words(word_dict, user_length)
for word in long_words:
    print(word)